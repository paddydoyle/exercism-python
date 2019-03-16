import re
from string import ascii_uppercase


class SgfTree(object):
    def __init__(self, properties=None, children=None):
        self.properties = properties or {}
        self.children = children or []

    def __eq__(self, other):
        if not isinstance(other, SgfTree):
            return False
        for k, v in self.properties.items():
            if k not in other.properties:
                return False
            if other.properties[k] != v:
                return False
        for k in other.properties.keys():
            if k not in self.properties:
                return False
        if len(self.children) != len(other.children):
            return False
        for a, b in zip(self.children, other.children):
            if a != b:
                return False
        return True

    def __ne__(self, other):
        return not self == other


def parse(s, is_root=True):
    """
    Recursive parsing function. Add a second parameter 'is_root'
    to deal with the fact that the enclosing parentheses are optional
    for children, but not for the root node.
    """

    # Parsing strategy:
    # - start with trivial cases
    # - then for the root tree, parse out the property substring
    #   - pass that for actual parsing to helper functions
    # - if there is any remainder, then look for child trees and
    #   if found, then recursively call this function on them
    #   - and add them as children to the root tree

    # Trivial edge cases: no input
    if not s:
        raise ValueError('Empty input')

    # Trivial edge cases: malformed parentheses
    if s == '()':
        raise ValueError('Missing semi-colon: "{}"'.format(s))

    # Trivial edge cases: trivial empty tree
    if s == '(;)':
        return SgfTree()

    # First look for enclosing parentheses, but only for the root node
    if is_root and not re.match(r'^ \( .+ \) $', s, flags=re.X | re.S):
        raise ValueError('Root must be surrounded by parentheses')

    # TODO: can the loop be replaced by re.findall() or re.finditer()
    # TODO: can the sub-parsing of _parse_properties() and
    #   _parse_property_values() be done by better groups in this first
    #   regex?? (there is quite a bit of repetition across the compiled
    #   regexes, but they are not _exactly_ the same). Maybe... but my
    #   head hurts from figuring out the parsing here, and am happy
    #   enough to leave it alone for now!

    # Extract properties, either:
    #   (;A[b]) # single key-value
    #   (;A[b][c]) # single key-multiple-values
    #   (;A[b]C[d]) # multiple key-multiple-values
    # and surrounding parentheses are optional (when not is_root)
    # Remaining child trees will be dealt with by recursive call.
    pattern = re.compile(r"""^
                              \(?            # optional opening paren
                              ;              # opening semi-colon
                              (              # start group..
                               (?:           #  start non-capturing group..
                                [A-Z]+       #   key, must be uppercase
                                (?:          #   start n-c group: '[..'
                                 \[          #     opening '['
                                   (?:       #     start n-c group
                                    \\\]     #      either '\]'
                                    |        #      or
                                    [^\]]    #      not a ']'
                                   )+        #     end n-c group
                                 \]          #     closing ']'
                                )+           #   end n-c group.. '[b]'
                               )+            #  end n-c group.. 'A[b]'
                              )              # end group
                              \)?            # optional closing paren
                          """, re.X | re.S)

    match = pattern.search(s)

    if not match:
        raise ValueError('Unable to parse the input string')

    # Match all of the properties 'A[b]', 'A[b]C[d]', 'A[b][c][d]' etc
    property_string = match.group(1)

    # Turn that string into a dict
    properties = _parse_properties(property_string)

    children = []

    # do we have any children left in the string?
    remainder = s[match.end():]

    while remainder:
        # Basic parsing of the child tree:
        # - optional surrounding parentheses
        # - must start with ;
        child_match = re.match(r"""^
                                    (        # start group
                                     \(?     # optional opening paren
                                     ;       # ;
                                     [^;)]+  # not ; or closing paren
                                     \)?     # optional closing paren
                                    )""",
                               remainder,
                               flags=re.X | re.S)

        if child_match:

            # recursive call, (is_root = False)
            child = parse(child_match.group(1), False)

            children.append(child)

            # progress the loop
            remainder = remainder[child_match.end():]
        else:
            break

    return SgfTree(properties, children)


def _parse_properties(s):
    """
    Convert a string of the format "(A([b])+)+" (e.g. "A[b]",
    "A[b][c]", "A[b]C[d]")
    into a dict of key-values, with the outer uppercase letters
    being the keys, and the list of values inside the []s as
    the dict values.
    """

    # TODO: can the loop be replaced by re.findall() or re.finditer()

    properties = {}

    # Extract each key-value pair. This can be of the form:
    # A[b] => becomes 'A'=match.group(1) and '[b]'=match.group(2)
    # A[b][c][d] => becomes 'A'=match.group(1) and '[b][c][d]' group(2)
    # The next key-value pairs will be dealt with by the loop.
    pattern = re.compile(r"""^
                              ([A-Z]+)     # group: key, must be uppercase
                              (            # start group for values
                               (?:         #  start n-c group
                                  \[       #   starts with '['
                                  (?:      #   start n-c group
                                     \\\]  #    either '\]'
                                     |     #    or
                                     [^\]] #    not a ']'
                                  )+       #   end n-c group, multiple
                                  \]       #   ends with ']'
                               )+          #  end n-c group.. multiple
                              )            # end values group
                          """, re.X | re.S)

    # do-while loop
    match = pattern.search(s)

    while match:
        key = match.group(1)
        values = match.group(2)

        values_list = _parse_property_values(values)

        properties[key] = values_list

        # progress the loop
        s = s[match.end():]
        match = pattern.search(s)

    return properties


def _parse_property_values(s):
    """
    Convert a string of the format "[a]+" (e.g. "[a]", "[a][b]")
    into a list of strings.
    For example '[a]' becomes the list: ['a']
    For example '[a][b]' becomes the list: ['a', 'b']
    """

    # TODO: can the loop be replaced by re.findall() or re.finditer()

    values = []

    # Extract a single value inside square brackets. Any remaining
    # values in square brackets are dealt with by the loop.
    pattern = re.compile(r"""^
                              \[              # starts with '['
                               (              # start group for values
                                (?:           #  start n-c group
                                   \\\]       #   either '\]'
                                   |          #   or
                                   [^\]]      #   not a ']'
                                )+            #  end n-c group, multiple chars
                               )              # end values group
                              \]              # ends with ']'
                          """, re.X | re.S)

    # do-while loop
    match = pattern.search(s)

    while match:
        value = match.group(1)

        # strip out the '\]' escape char, if any
        value = value.replace(r'\]', ']')

        # replace '\t' with space, if any
        value = value.replace('\t', ' ')

        values.append(value)

        # progress the loop
        s = s[match.end():]
        match = pattern.search(s)

    return values
