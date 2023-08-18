from enum import Enum

class Workclass(str, Enum):
    Federal_gov = 'Federal-gov',
    Local_gov = 'Local-gov',
    Never_worked = 'Never-worked',
    Private = 'Private',
    Self_emp_inc = 'Self-emp-inc',
    Self_emp_not_inc = 'Self-emp-not-inc',
    State_gov = 'State-gov',
    Without_pay = 'Without-pay'


class Education(str, Enum):
    Tenth = '10th',
    Eleventh = '11th',
    Twelvth = '12th',
    FirstFourth = '1st-4th',
    FifthSixt = '5th-6th',
    SeventhEight = '7th-8th',
    Nineth = '9th',
    Assoc_acdm = 'Assoc-acdm',
    Assoc_voc = 'Assoc-voc',
    Bachelors = 'Bachelors',
    Doctorate = 'Doctorate',
    HS_grad = 'HS-grad',
    Masters = 'Masters',
    Preschool = 'Preschool',
    Prof_school = 'Prof-school',
    Some_college = 'Some-college'


class Marital(str, Enum):
    Divorced = 'Divorced',
    Married_AF_spouse = 'Married-AF-spouse',
    Married_civ_spouse = 'Married-civ-spouse',
    Married_spouse_absent = 'Married-spouse-absent',
    Never_married = 'Never-married',
    Separated = 'Separated',
    Widowed = 'Widowed'


class Occupation(str, Enum):
    q = '?',
    Adm_clerical = 'Adm-clerical',
    Armed_Forces = 'Armed-Forces',
    Craft_repair = 'Craft-repair',
    Exec_managerial = 'Exec-managerial',
    Farming_fishing = 'Farming-fishing',
    Handlers_cleaners = 'Handlers-cleaners',
    Machine_op_inspct = 'Machine-op-inspct',
    Other_service = 'Other-service',
    Priv_house_serv = 'Priv-house-serv',
    Prof_specialty = 'Prof-specialty',
    Protective_serv = 'Protective-serv',
    Sales = 'Sales',
    Tech_support = 'Tech-support',
    Transport_moving = 'Transport-moving'


class Sex(str, Enum):
    Female = "Female"
    Male = "Male"


class Relationship(str, Enum):
    Husband = 'Husband',
    Not_in_family = 'Not-in-family',
    Other_relative = 'Other-relative',
    Own_child = 'Own-child',
    Unmarried = 'Unmarried',
    Wife = 'Wife'


class Race(str, Enum):
    Amer_Indian_Eskimo = "Amer-Indian-Eskimo",
    Asian_Pac_Islander = "Asian-Pac-Islander",
    Black = "Black",
    Other = "Other",
    White = "White"


class Country(str, Enum):
    Cambodia = 'Cambodia',
    Canada = 'Canada',
    China = 'China',
    Columbia = 'Columbia',
    Cuba = 'Cuba',
    Dominican_Republic = 'Dominican-Republic',
    Ecuador = 'Ecuador',
    El_Salvador = 'El-Salvador',
    England = 'England',
    France = 'France',
    Germany = 'Germany',
    Greece = 'Greece',
    Guatemala = 'Guatemala',
    Haiti = 'Haiti',
    Holand_Netherlands = 'Holand-Netherlands',
    Honduras = 'Honduras',
    Hong = 'Hong',
    Hungary = 'Hungary',
    India = 'India',
    Iran = 'Iran',
    Ireland = 'Ireland',
    Italy = 'Italy',
    Jamaica = 'Jamaica',
    Japan = 'Japan',
    Laos = 'Laos',
    Mexico = 'Mexico',
    Nicaragua = 'Nicaragua',
    Outlying = 'Outlying-US(Guam-USVI-etc)',
    Peru = 'Peru',
    Philippines = 'Philippines',
    Poland = 'Poland',
    Portugal = 'Portugal',
    Puerto_Rico = 'Puerto-Rico',
    Scotland = 'Scotland',
    South = 'South',
    Taiwan = 'Taiwan',
    Thailand = 'Thailand',
    Trinadad = 'Trinadad&Tobago',
    United_States = 'United-States',
    Unknown = '?',
    Vietnam = 'Vietnam',
    Yugoslavia = 'Yugoslavia'
