class Elements:
    def __init__(self,symbol,name,atomic_number,mass,metal_property,standard_state,charge):
        self.symbol = symbol
        self.atomic_number = atomic_number
        self.mass = mass
        self.metal_property = metal_property
        self.standard_state = standard_state
        self.charge = charge
        self.name = name

elements = {

"H" : Elements("H","Hydrogen",1,1.008,"NON-Metal","Gas",+1),
"He" : Elements("He","Helium",2,4.003,"NON-Metal","Gas",0),
"Li" : Elements("Li","Lithium",3,6.941,"Metal","Solid",+1),
"Be" : Elements("Be","Beryllium",4,9.012,"Metal","Solid",+2),
"B" : Elements("B","Boron",5,10.811,"Metalloid","Solid",+3),
"C" : Elements("C","Carbon",6,12.011,"NON-Metal","Solid","+4,-4"),
"N" : Elements("N","Nitrogen",7,14.007,"NON-Metal","Gas",-3),
"O" : Elements("O","Oxygen",8,15.999,"NON-Metal","Gas",-2),
"F" : Elements("F","Fluorine",9,18.998,"NON-Metal","Gas",-1),
"Ne": Elements("Ne","Neon",10,20.180,"NON-Metal","Gas",0),

"Na": Elements("Na","Sodium",11,22.990,"Metal","Solid",+1),
"Mg": Elements("Mg","Magnesium",12,24.305,"Metal","Solid",+2),
"Al": Elements("Al","Aluminum",13,26.982,"Metal","Solid",+3),
"Si": Elements("Si","Silicon",14,28.085,"Metalloid","Solid","-4,+2,+4"),
"P" : Elements("P","Phosphorus",15,30.974,"NON-Metal","Solid","-3,+3,+5"),
"S" : Elements("S","Sulfur",16,32.06,"NON-Metal","Solid","-2,+2,+4,+6"),
"Cl": Elements("Cl","Chlorine",17,35.45,"NON-Metal","Gas","-1,+1,+3,+5,+7"),
"Ar": Elements("Ar","Argon",18,39.948,"NON-Metal","Gas",0),

"K" : Elements("K","Potassium",19,39.098,"Metal","Solid",+1),
"Ca": Elements("Ca","Calcium",20,40.078,"Metal","Solid",+2),
"Sc": Elements("Sc","Scandium",21,44.956,"Metal","Solid",+3),
"Ti": Elements("Ti","Titanium",22,47.867,"Metal","Solid","+2,+3,+4"),
"V" : Elements("V","Vanadium",23,50.942,"Metal","Solid","+2,+3,+4,+5"),
"Cr": Elements("Cr","Chromium",24,51.996,"Metal","Solid","+2,+3,+6"),
"Mn": Elements("Mn","Manganese",25,54.938,"Metal","Solid","+2,+3,+4,+6,+7"),
"Fe": Elements("Fe","Iron",26,55.845,"Metal","Solid","+2,+3"),
"Co": Elements("Co","Cobalt",27,58.933,"Metal","Solid","+2,+3"),
"Ni": Elements("Ni","Nickel",28,58.693,"Metal","Solid","+2,+3"),
"Cu": Elements("Cu","Copper",29,63.546,"Metal","Solid","+1,+2"),
"Zn": Elements("Zn","Zinc",30,65.38,"Metal","Solid",+2),
"Ga": Elements("Ga","Gallium",31,69.723,"Metal","Solid","+1,+3"),
"Ge": Elements("Ge","Germanium",32,72.630,"Metalloid","Solid","-4,+2,+4"),
"As": Elements("As","Arsenic",33,74.922,"Metalloid","Solid","-3,+3,+5"),
"Se": Elements("Se","Selenium",34,78.971,"NON-Metal","Solid","-2,+4,+6"),
"Br": Elements("Br","Bromine",35,79.904,"NON-Metal","Liquid","-1,+1,+3,+5,+7"),
"Kr": Elements("Kr","Krypton",36,83.798,"NON-Metal","Gas","0,+2"),

"Rb": Elements("Rb","Rubidium",37,85.468,"Metal","Solid",+1),
"Sr": Elements("Sr","Strontium",38,87.62,"Metal","Solid",+2),
"Y" : Elements("Y","Yttrium",39,88.906,"Metal","Solid",+3),
"Zr": Elements("Zr","Zirconium",40,91.224,"Metal","Solid",+4),
"Nb": Elements("Nb","Niobium",41,92.906,"Metal","Solid","+3,+5"),
"Mo": Elements("Mo","Molybdenum",42,95.95,"Metal","Solid","+2,+3,+4,+5,+6"),
"Tc": Elements("Tc","Technetium",43,98,"Metal","Solid","+4,+7"),
"Ru": Elements("Ru","Ruthenium",44,101.07,"Metal","Solid","+3,+4"),
"Rh": Elements("Rh","Rhodium",45,102.91,"Metal","Solid","+3"),
"Pd": Elements("Pd","Palladium",46,106.42,"Metal","Solid","+2,+4"),
"Ag": Elements("Ag","Silver",47,107.87,"Metal","Solid","+1"),
"Cd": Elements("Cd","Cadmium",48,112.41,"Metal","Solid",+2),
"In": Elements("In","Indium",49,114.82,"Metal","Solid","+1,+3"),
"Sn": Elements("Sn","Tin",50,118.71,"Metal","Solid","+2,+4"),
"Sb": Elements("Sb","Antimony",51,121.76,"Metalloid","Solid","-3,+3,+5"),
"Te": Elements("Te","Tellurium",52,127.60,"Metalloid","Solid","-2,+4,+6"),
"I" : Elements("I","Iodine",53,126.90,"NON-Metal","Solid","-1,+1,+3,+5,+7"),
"Xe": Elements("Xe","Xenon",54,131.29,"NON-Metal","Gas","0,+2,+4,+6,+8"),

"Cs": Elements("Cs","Cesium",55,132.91,"Metal","Solid",+1),
"Ba": Elements("Ba","Barium",56,137.33,"Metal","Solid",+2),
"La": Elements("La","Lanthanum",57,138.91,"Metal","Solid","+3"),
"Ce": Elements("Ce","Cerium",58,140.12,"Metal","Solid","+3,+4"),
"Pr": Elements("Pr","Praseodymium",59,140.91,"Metal","Solid","+3"),
"Nd": Elements("Nd","Neodymium",60,144.24,"Metal","Solid","+3"),
"Pm": Elements("Pm","Promethium",61,145,"Metal","Solid","+3"),
"Sm": Elements("Sm","Samarium",62,150.36,"Metal","Solid","+2,+3"),
"Eu": Elements("Eu","Europium",63,151.96,"Metal","Solid","+2,+3"),
"Gd": Elements("Gd","Gadolinium",64,157.25,"Metal","Solid","+3"),
"Tb": Elements("Tb","Terbium",65,158.93,"Metal","Solid","+3"),
"Dy": Elements("Dy","Dysprosium",66,162.50,"Metal","Solid","+3"),
"Ho": Elements("Ho","Holmium",67,164.93,"Metal","Solid","+3"),
"Er": Elements("Er","Erbium",68,167.26,"Metal","Solid","+3"),
"Tm": Elements("Tm","Thulium",69,168.93,"Metal","Solid","+3"),
"Yb": Elements("Yb","Ytterbium",70,173.05,"Metal","Solid","+2,+3"),
"Lu": Elements("Lu","Lutetium",71,174.97,"Metal","Solid","+3"),

"Hf": Elements("Hf","Hafnium",72,178.49,"Metal","Solid","+4"),
"Ta": Elements("Ta","Tantalum",73,180.95,"Metal","Solid","+5"),
"W" : Elements("W","Tungsten",74,183.84,"Metal","Solid","+4,+6"),
"Re": Elements("Re","Rhenium",75,186.21,"Metal","Solid","+4,+6,+7"),
"Os": Elements("Os","Osmium",76,190.23,"Metal","Solid","+4,+8"),
"Ir": Elements("Ir","Iridium",77,192.22,"Metal","Solid","+3,+4"),
"Pt": Elements("Pt","Platinum",78,195.08,"Metal","Solid","+2,+4"),
"Au": Elements("Au","Gold",79,196.97,"Metal","Solid","+1,+3"),
"Hg": Elements("Hg","Mercury",80,200.59,"Metal","Liquid","+1,+2"),
"Tl": Elements("Tl","Thallium",81,204.38,"Metal","Solid","+1,+3"),
"Pb": Elements("Pb","Lead",82,207.2,"Metal","Solid","+2,+4"),
"Bi": Elements("Bi","Bismuth",83,208.98,"Metal","Solid","+3,+5"),
"Po": Elements("Po","Polonium",84,209,"Metal","Solid","+2,+4"),
"At": Elements("At","Astatine",85,210,"Metalloid","Solid","-1,+1,+3,+5,+7"),
"Rn": Elements("Rn","Radon",86,222,"NON-Metal","Gas",0),

"Fr": Elements("Fr","Francium",87,223,"Metal","Solid",+1),
"Ra": Elements("Ra","Radium",88,226,"Metal","Solid",+2),
"Ac": Elements("Ac","Actinium",89,227,"Metal","Solid","+3"),
"Th": Elements("Th","Thorium",90,232.04,"Metal","Solid","+4"),
"Pa": Elements("Pa","Protactinium",91,231.04,"Metal","Solid","+4,+5"),
"U" : Elements("U","Uranium",92,238.03,"Metal","Solid","+4,+6"),
"Np": Elements("Np","Neptunium",93,237,"Metal","Solid","+3,+4,+5,+6"),
"Pu": Elements("Pu","Plutonium",94,244,"Metal","Solid","+3,+4,+5,+6"),
"Am": Elements("Am","Americium",95,243,"Metal","Solid","+3"),
"Cm": Elements("Cm","Curium",96,247,"Metal","Solid","+3"),
"Bk": Elements("Bk","Berkelium",97,247,"Metal","Solid","+3,+4"),
"Cf": Elements("Cf","Californium",98,251,"Metal","Solid","+3"),
"Es": Elements("Es","Einsteinium",99,252,"Metal","Solid","+3"),
"Fm": Elements("Fm","Fermium",100,257,"Metal","Solid","+3"),
"Md": Elements("Md","Mendelevium",101,258,"Metal","Solid","+3"),
"No": Elements("No","Nobelium",102,259,"Metal","Solid","+2,+3"),
"Lr": Elements("Lr","Lawrencium",103,266,"Metal","Solid","+3"),

"Rf": Elements("Rf","Rutherfordium",104,267,"Metal","Solid","+4"),
"Db": Elements("Db","Dubnium",105,268,"Metal","Solid","+5"),
"Sg": Elements("Sg","Seaborgium",106,269,"Metal","Solid","+6"),
"Bh": Elements("Bh","Bohrium",107,270,"Metal","Solid","+7"),
"Hs": Elements("Hs","Hassium",108,277,"Metal","Solid","+8"),
"Mt": Elements("Mt","Meitnerium",109,278,"Metal","Solid","+3"),
"Ds": Elements("Ds","Darmstadtium",110,281,"Metal","Solid","+2,+4"),
"Rg": Elements("Rg","Roentgenium",111,282,"Metal","Solid","+1,+3"),
"Cn": Elements("Cn","Copernicium",112,285,"Metal","Solid","+2"),
"Nh": Elements("Nh","Nihonium",113,286,"Metal","Solid","+1,+3"),
"Fl": Elements("Fl","Flerovium",114,289,"Metal","Solid","+2,+4"),
"Mc": Elements("Mc","Moscovium",115,290,"Metal","Solid","+1,+3"),
"Lv": Elements("Lv","Livermorium",116,293,"Metal","Solid","+2"),
"Ts": Elements("Ts","Tennessine",117,294,"Metalloid","Solid","-1,+1,+3,+5,+7"),
"Og": Elements("Og","Oganesson",118,294,"NON-Metal","Gas",0),

}


def printall(element):
    print("Symbol: ",element.symbol)
    print("Name: ",element.name)
    print("Atomic Number: ",element.atomic_number)
    print("Mass: ",element.mass)
    print("metal properties: ",element.metal_property)
    print("Standard state: ",element.standard_state)
    print("Charges: ", element.charge)
    
def menu():

    print("1.Symbol")
    print("2.Atomic number")
    choice = int(input(" 1 or 2 "))

    if choice == 1:
        symbol = input("Enter element symbol: ").capitalize()
        element = elements.get(symbol)
        if element:
            printall(element)
        else:
            print("Element not found")

    elif choice == 2:
        Number = int(input("Enter atomic number: "))
        element_list = list(elements.values())

        if 1 <= Number <= len(element_list):
            ATM = element_list[Number - 1] 
            printall(ATM)
        else:
            print("Element not found")

    else:
        print("Element not found")
        

menu()