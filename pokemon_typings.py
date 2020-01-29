"""Pokemon Typings: Allows for all combat relationships between Pokemon types."""

def interactions(type1, type2=None):
    if type2 == None:
        return monotype(type1)
    else:
        print(type1().type + '/' + type2().type + ' pokemon are strong against ' + str(type1().strengths + type2().strengths) + '.')
        print()
        print(type1().type + '/' + type2().type + ' pokemon are ineffective against ' + str(type1().ineffective + type2().ineffective) + '.')
        print()
        print(type1().type + '/' + type2().type + ' pokemon are weak against ' + str(type1().weaknesses + type2().weaknesses) + '.')
        print()
        print(type1().type + '/' + type2().type + ' pokemon are resistant against ' + str(type1().resistances + type2().resistances) + '.')
        print()
        print(type1().type + '/' + type2().type + ' pokemon are immune to ' + str(type1().immunities_to + type2().immunities_to) + '.')
        print()
        print(type1().type + '/' + type2().type + ' pokemon are immune against ' + str(type1().immunities_against + type1().immunities_against) + '.')

def monotype(type1):
    print(type1().type + ' pokemon are strong against ' + str(type1().strengths) + '.')
    print()
    print(type1().type + ' pokemon are ineffective against ' + str(type1().ineffective) + '.')
    print()
    print(type1().type + ' pokemon are weak against ' + str(type1().weaknesses) + '.')
    print()
    print(type1().type + ' pokemon are resistant against ' + str(type1().resistances) + '.')
    print()
    print(type1().type + ' pokemon are immune to ' + str(type1().immunities_to) + '.')
    print()
    print(type1().type + ' pokemon are immune against ' + str(type1().immunities_against) + '.')

"""def dualtype(type1, type2):
    two_strong, two_resistant, four_resistant, two_weak, four_weak, immune_to, immune_against = [], [], [], [], [], [], []
    two_strong.append(type1.strengths)
    for item in type2.strengths
        if item not in two_strong
            two_strong.append(item)
    immune_to.append(immunities_to)
    for item in type2.immunities_to
        if item not in immune_to:
            immune_to.append(item)"""

### Pokemon Library and Types ###

class Pokemon(object):
    """A general Type class that determines commonalities between all types"""
    strengths = []
    ineffective = []
    weaknesses = []
    resistances = []
    immunities_to = []
    immunities_against = []

    def __init__(self, type1, type2=None):
        if type2 == None:
            self.type = type1().type
            self.strengths = type1().strengths
            self.ineffective = type1().ineffective
            self.weaknesses = type1().weaknesses
            self.resistances = type1().resistances
            self.immunities_to = type1().immunities_to
            self.immunities_against = type1().immunities_against
        else:
            self.type = type1().type + type2().type
            self.strengths = type1().strengths + type2().strengths
            self.ineffective = type1().ineffective + type2().ineffective
            self.weaknesses = type1().weaknesses + type2().weaknesses
            self.resistances = type1().resistances + type2().resistances
            self.immunities_to = type1().immunities_to + type2().immunities_to
            self.immunities_against = type1().immunities_against + type2().immunities_against

class Normal(Pokemon):
    """Normal-types are not strong against any types. They are only weak against
    Fighting-types. They are not resistant to any types. Normal-types are immune
    to Ghost-types and vice versa."""

    def __init__(self):
        self.type = 'Normal'
        self.weaknesses = ['Fighting-types']
        self.immunities_to = ['Ghost-types']
        self.immunities_against = ['Ghost-types']

class Fighting(Pokemon):
    """Fighting-types are strong against Normal, Rock, Steel, Ice, and Dark.
    They are weak to Psychic, Flying, and Fairy. They are resistant to Rock,
    Bug, and Dark. Fighting-types are not immune to any types, but immune against
    Ghost-types."""

    def __init__(self):
        self.type = 'Fighting'
        self.strengths = ['Normal-types', 'Rock-types', 'Steel-types', 'Ice-types', 'Dark-types']
        self.ineffective = ['Flying-types', 'Poison-types', 'Bug-types', 'Psychic-types', 'Fairy-types']
        self.weaknesses = ['Psychic-types', 'Flying-types', 'Fairy-types']
        self.resistances = ['Rock', 'Bug', 'Dark']
        self.immunities_against = ['Ghost-types']

class Flying(Pokemon):
    """Flying-types are strong against Fighting, Bug, and Grass. They are weak
    against Rock, Electric, and Ice. They are resistant to Fighting, Bug, and Grass.
    Flying-types are immune to Ground."""

    def __init__(self):
        self.type = 'Flying'
        self.strengths = ['Fighting-types', 'Bug-types', 'Grass-types']
        self.ineffective = ['Rock-types', 'Steel-types', 'Electric-types']
        self.weaknesses = ['Rock-types', 'Electric-types', 'Ice-types']
        self.resistances = ['Fighting-types', 'Bug-types', 'Grass-types']
        self.immunities_to = ['Ground-types']

class Poison(Pokemon):
    """Poison-types are strong against Grass and Fairy. They are weak against Ground
    and Psychic. They are resistant to Fighting, Poison, Bug, Grass, and Fairy.
    Poison-types are immune against Steel-types."""

    def __init__(self):
        self.type = 'Poison'
        self.strengths = ['Grass-types', 'Fairy-types']
        self.ineffective = ['Poison-types', 'Ground-types', 'Rock-types', 'Ghost-types']
        self.weaknesses = ['Ground-types', 'Psychic-types']
        self.resistances = ['Fighting-types', 'Poison-types', 'Bug-types', 'Grass-types', 'Fairy-types']
        self.immunities_against = ['Steel-types']

class Ground(Pokemon):
    """Ground-types are strong against Poison, Rock, Steel, Fire, and Electric.
    They are weak against Water, Grass, and Ice. They are resistant to Poison, Rock,
    Fighting, Bug, and Grass. Ground-types are immune to electric and immune against
    Flying-types."""

    def __init__(self):
        self.type = 'Ground'
        self.strengths = ['Poison-types', 'Rock-types', 'Steel-types', 'Fire-types', 'Electric-types']
        self.ineffective = ['Bug-types', 'Grass-types']
        self.weaknesses = ['Water-types', 'Grass-types', 'Ice-types']
        self.resistances = ['Poison-types', 'Rock-types']
        self.immunities_to = ['Electric-types']
        self.immunities_against = ['Flying-types']

class Rock(Pokemon):
    """Rock-types are strong against Flying, Bug, Fire, and Ice. They are weak against
    Fighting, Ground, Steel, Water, and Grass. They are resistant to Normal, Flying, Poison,
    and Fire. Rock-types have no immunities to or against anything."""

    def __init__(self):
        self.type = 'Rock'
        self.strengths = ['Flying-types', 'Bug-types', 'Fire-types', 'Ice-types']
        self.ineffective = ['Fighting-types', 'Ground-types', 'Steel-types']
        self.weaknesses = ['Fighting-types', 'Ground-types', 'Steel-types', 'Water-types', 'Grass-types']
        self.resistances = ['Normal-types', 'Flying-types', 'Poison-types', 'Fire-types']

class Bug(Pokemon):
    """Bug-types are strong against Grass, Psychic, and Dark. They are weak against
    Flying, Rock, and Fire. They are resistant to Fighting, Ground, and Grass. Bug-types
    have no immunities to or against anything."""

    def __init__(self):
        self.type = 'Bug'
        self.strengths = ['Grass-types', 'Psychic-types', 'Dark-types']
        self.ineffective = ['Fighting-types', 'Flying-types', 'Poison-types', 'Ghost-types', 'Steel-types', 'Fire-types', 'Fairy-types']
        self.weaknesses = ['Flying-types', 'Rock-types', 'Fire-types']
        self.resistances = ['Fighting-types', 'Ground-types', 'Grass-types']

class Ghost(Pokemon):
    """Ghost-types are strong against Ghost and Psychic. They are weak against Ghost, and Dark
    They are resistant to Poison and Bug. Ghost types are immune to Normal and Fighting and
    immune against Normal."""

    def __init__(self):
        self.type = 'Ghost'
        self.strengths = ['Ghost-types', 'Psychic-types']
        self.ineffective = ['Dark-types']
        self.weaknesses = ['Ghost-types', 'Dark-types']
        self.resistances = ['Poison-types', 'Bug-types']
        self.immunities_to = ['Normal-types', 'Fighting-types']
        self.immunities_against = ['Normal-types']

class Steel(Pokemon):
    """Steel-types are strong against Rock, Ice, and Fairy. They are weak against Fighting,
    Ground, and Fire. They are resistant to Normal, Flying, Rock, Bug, Steel, Grass, Psychic,
    Ice, Dragon, and Fairy. Steel-types are immune to Poison."""

    def __init__(self):
        self.type = 'Steel'
        self.strengths = ['Rock-types', 'Ice-types', 'Fairy-types']
        self.ineffective = ['Steel-types', 'Fire-types', 'Water-types', 'Electric-types']
        self.weaknesses = ['Fighting-types', 'Ground-types', 'Fire-types']
        self.resistances = ['Normal-types', 'Flying-types', 'Rock-types', 'Bug-types', 'Steel-types', 'Grass-types', 'Psychic-types', 'Ice-types', 'Dragon-types', 'Fairy-types']
        self.immunities_to = ['Poison-types']

class Fire(Pokemon):
    """Fire-types are strong against Bug, Steel, Grass, and Ice. They are weak against Ground,
    Rock, and Water. They are resistant to Bug, Steel, Fire, Grass, Ice, and Fairy. Fire-types
    have no immunities to or against anything."""

    def __init__(self):
        self.type = 'Fire'
        self.strengths = ['Bug-types', 'Steel-types', 'Grass-types', 'Ice-types']
        self.ineffective = ['Rock-types', 'Fire-types', 'Water-types', 'Dragon-types']
        self.weaknesses = ['Ground-types', 'Rock-types', 'Water-types']
        self.resistances = ['Bug-types', 'Steel-types', 'Fire-types', 'Grass-types', 'Ice-types', 'Fairy-types']

class Water(Pokemon):
    """Water-types are strong against Ground, Rock, Fire. They are weak against Grass, and Electric.
    They are resistant to Steel, Fire, Water, and Ice. Water-types have no immunities to or against
    anything."""

    def __init__(self):
        self.type = 'Water'
        self.strengths = ['Ground-types', 'Rock-types', 'Fire-types']
        self.ineffective = ['Water-types', 'Grass-types', 'Dragon-types']
        self.weaknesses = ['Grass-types', 'Electric-types']
        self.resistances = ['Steel-types', 'Fire-types', 'Water-types', 'Ice-types']

class Grass(Pokemon):
    """Grass-types are strong against Ground, Rock, and Water. They are weak against Flying, Poison,
    Bug, Fire, and Ice. They are resistant to Ground, Water, Grass, and Electric. Grass types have
    no immunities to or against anything."""

    def __init__(self):
        self.type = 'Grass'
        self.strengths = ['Ground-types', 'Rock-types', 'Water-types']
        self.ineffective = ['Flying-types', 'Poison-types', 'Bug-types', 'Steel-types', 'Fire-types', 'Grass-types', 'Dragon-types']
        self.weaknesses = ['Flying-types', 'Poison-types', 'Bug-types', 'Fire-types', 'Ice-types']
        self.resistances = ['Ground-types', 'Water-types', 'Grass-types', 'Electric-types']

class Electric(Pokemon):
    """Electric-types are strong against Flying and Water. They are weak against Ground only.
    They are resistant to Flying, Steel, and Electric. Electric types are not immune to anything,
    but are immune against Ground."""

    def __init__(self):
        self.type = 'Electric'
        self.strengths = ['Flying-types', 'Water-types']
        self.ineffective = ['Grass-types', 'Electric-type', 'Dragon-type']
        self.weaknesses = ['Ground-types']
        self.resistances = ['Flying-types', 'Steel-types', 'Electric-types']
        self.immunities_against = ['Ground-types']

class Psychic(Pokemon):
    """Psychic-types are strong against Fighting and Poison. They are weak against Bug, Ghost,
    and Dark. They are resistant to Fighting and Psychic. Psychic-types are not immune to anything
    but are immune against Dark."""

    def __init__(self):
        self.type = 'Psychic'
        self.strengths = ['Fighting-types', 'Poison-types']
        self.ineffective = ['Steel-types', 'Psychic-types']
        self.weaknesses = ['Bug-types', 'Ghost-types', 'Dark-types']
        self.resistances = ['Fighting-types', 'Psychic-types']
        self.immunities_against = ['Dark-types']

class Ice(Pokemon):
    """Ice-types are strong against Flying, Ground, Grass, and Dragon. They are weak against
    Fighting, Rock, Steel, and Fire. They are resistant to Ice only. Ice-types are not immune
    to or against anything."""

    def __init__(self):
        self.type = 'Ice'
        self.strengths = ['Flying-types', 'Ground-types', 'Grass-types', 'Dragon-types']
        self.ineffective = ['Steel-types', 'Fire-types', 'Water-types', 'Ice-types']
        self.weaknesses = ['Fighting-types', 'Rock-types', 'Steel-types', 'Fire-types']
        self.resistances = ['Ice-types']

class Dragon(Pokemon):
    """Dragon-types are strong against Dragon only. They are weak against Ice, Dragon, and
    Fairy. They are resistant to Fire, Water, Grass, and Electric. Dragon types are immune
    against Fairy-types only."""

    def __init__(self):
        self.type = 'Dragon'
        self.strengths = ['Dragon-types']
        self.ineffective = ['Steel-types']
        self.weaknesses = ['Ice-types', 'Dragon-types', 'Fairy-types']
        self.resistances = ['Fire-types', 'Water-types', 'Grass-types', 'Electric-types']
        self.immunities_against = ['Fairy-types']

class Dark(Pokemon):
    """Dark-types are strong against Ghost and Psychic. They are weak against Fighting, Bug,
    and Fairy. They are resistant to Ghost and Dark. Dark-types are immune to Psychic, but
    are not immune against anything."""

    def __init__(self):
        self.type = 'Dark'
        self.strengths = ['Ghost-types', 'Psychic-types']
        self.ineffective = ['Fighting-types', 'Dark-types', 'Fairy-types']
        self.weaknesses = ['Fighting-types', 'Bug-types', 'Fairy-types']
        self.resistances = ['Ghost-types', 'Dark-types']
        self.immunities_to = ['Psychic-types']

class Fairy(Pokemon):
    """Fairy-types are strong against Fighting, Dragon, and Dark. They are weak against Poison
    and Steel. They are resistant to Fighting, Bug, and Dark. Fairy-types are immune to Dragon,
    but are not immune against anything."""

    def __init__(self):
        self.type = 'Fairy'
        self.strengths = ['Fighting-types', 'Dragon-types', 'Dark-types']
        self.ineffective = ['Poison-types', 'Steel-types', 'Fire-types']
        self.weaknesses = ['Poison-types', 'Steel-types']
        self.resistances = ['Fighting-types', 'Bug-types', 'Dark-types']
        self.immunities_to = ['Dragon-types']

class NullType(Pokemon):
    """The NullType class serves as a placeholder for all monotype Pokemon."""

    def __init__(self):
        self.type = None
        self.strengths = None
        self.ineffective = None
        self.weaknesses = None
        self.resistances = None
        self.immunities_to = None
        self.immunities_against = None
