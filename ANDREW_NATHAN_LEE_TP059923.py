#ANDREW NATHAN LEE
#TP059923
def createInventory():
    bigLst = []
    count = 0
    print('Choose at least 3 sections below for the model!')
    print('1. Body work section (BWS)')
    print('2. Car engine section (CES)')
    print('3. Electronic section (ES)')
    print('4. Lighting section (LS)')
    print('5. Safety section (SS)')
    while True:
        section = 'section: ' + input('Please enter section name: [-1 to end]')
        if section == 'section: -1':
            break
        #if user enters -1, the program exits the outer loop
        else:
            print('Choose the components for each section!')            
            while True:
                name = 'name: ' + input('Enter name of component: [999 to end]')
                if name == 'name: 999':
                    break
                #if user enters 999, the program exits the inner loop
                else:
                    smallLst = []
                    identification = 'id: ' + input('Enter "XX01" for first component, "XX02" for second component and so on: ')
                    quantity = 'quantity: ' + input('Enter number of components available: ')
                    price = 'price: RM' + input('Enter price of each component: ')
                    material = 'material: ' + input('Enter material used to make the component: ')
                    supplier = 'supplier: ' + input('Enter supplier\'s company name: ')
                    smallLst.append(section)
                    smallLst.append(name)
                    smallLst.append(identification)
                    smallLst.append(quantity)
                    smallLst.append(price)
                    smallLst.append(material)
                    smallLst.append(supplier)
                bigLst.append(smallLst)        
            count += 1         
    if count < 3:#the inventory must have at least three sections
        print('You must enter at least three sections')
    return bigLst
#This function creates the part's details required to store in the Bios, Ambry and Barrier text files

def saveBiosInventory():
    try:
        fileHandler = open('bios_inventory.txt', 'w')
    except:
        print('File does not exist')
        exit()
    bios = createInventory()
    for component in bios:
        for detail in component:
            if detail.startswith('id: '):
                detail = detail.replace('XX', 'BS')
            fileHandler.write(detail + '    ')
        fileHandler.write('\n')
    fileHandler.close()
#This function saves the data created by the createInventory function into the 'bios_inventory.txt' file

def saveAmbryInventory():
    try:
        fileHandler = open('ambry_inventory.txt', 'w')
    except:
        print('File does not exist')
        exit()
    ambry = createInventory()
    for component in ambry:
        for detail in component:
            if detail.startswith('id: '):
                detail = detail.replace('XX', 'AY')
            fileHandler.write(detail + '    ')
        fileHandler.write('\n')
    fileHandler.close()
#This function saves the data created by the createInventory function into the 'ambry_inventory.txt' file
    
def saveBarrierInventory():
    try:
        fileHandler = open('barrier_inventory.txt', 'w')
    except:
        print('File does not exist')
        exit()
    barrier = createInventory()
    for component in barrier:
        for detail in component:
            if detail.startswith('id: '):
                detail = detail.replace('XX', 'BR')
            fileHandler.write(detail + '    ')
        fileHandler.write('\n')        
    fileHandler.close()
#This function saves the data created by the createInventory function into the 'barrier_inventory.txt' file    

def countFileLines(file):
    try:
        fileHandler = open(file, 'r')
    except:
        print('File does not exist')
        exit()
    count = 0
    for line in fileHandler:
        count += 1
    fileHandler.close()    
    return count
#This function counts the number of lines in each text file which is also the total number of components in each warehouse

def increaseQuantity(file, partCode, supplierName, amount):
    try:
        fileHandler = open(file, 'r')
    except:
        print('File does not exist')
        exit()
    newData = []
    for line in fileHandler:
        newLine = line.rstrip().split('    ')
        #newLine[2] stands for the list containing a particular part's id
        #newLine[3] stands for the list containing a particular part's quantity
        #newLine[6] stands for the list containing a particular part's supplier's name
        if newLine[2].split(': ')[1].upper() == partCode.upper() and newLine[6].split(': ')[1].upper() == supplierName.upper():
            newLine[3] = 'quantity: ' + str(int(newLine[3].split(': ')[1]) + amount)
        newData.append(newLine)
    fileHandler.close()
    try:
        fileHandlerTwo = open(file, 'w')
    except:
        print('File does not exist')
        exit()
    for component in newData:
        for detail in component:
            fileHandlerTwo.write(detail + '    ')
        fileHandlerTwo.write('\n')
    fileHandlerTwo.close()
#This function increases the quantity of a component according to the file name, part id, amount and supplier's name 

def decreaseQuantity(file, partCode, section, amount):
    try:
        fileHandler = open(file, 'r')
    except:
        print('File does not exist')
        exit()
    newData = []
    for line in fileHandler:
        newLine = line.rstrip().split('    ')
        #newLine[0] stands for the list containing a particular part's section number
        #newLine[2] stands for the list containing a particular part's id
        #newLine[3] stands for the list containing a particular part's quantity
        if newLine[0].split(': ')[1] == section and newLine[2].split(': ')[1].upper() == partCode.upper():
            left = int(newLine[3].split(': ')[1]) - amount
            if left < 0:
                return 'Invalid amount'
            else:
                newLine[3] = 'quantity: ' + str(left)
        newData.append(newLine)
    fileHandler.close()
    try:
        fileHandlerTwo = open(file, 'w')
    except:
        print('File does not exist')
        exit()
    for component in newData:
        for detail in component:
            fileHandlerTwo.write(detail + '    ')
        fileHandlerTwo.write('\n')
    fileHandlerTwo.close()
#This function decreases the quantity of a component according to the file name, part id, amount and section number
    
def updateInventory():
    for num in range(3):
        warehouse = input('Choose the warehouse to be updated in the given order: [bios(WBS), ambry(WAY), barrier(WBR)]')
        if warehouse.upper() == 'WBS':
            lineNum = countFileLines('bios_inventory.txt')
        elif warehouse.upper() == 'WAY':
            lineNum = countFileLines('ambry_inventory.txt')
        elif warehouse.upper() == 'WBR':
            lineNum = countFileLines('barrier_inventory.txt')
        else:
            print('Invalid warehouse code')
            continue
        for i in range(round(lineNum * 40 / 100)):
            #40 percent of the parts are updated (increased or decreased)
            identification = input('Enter component\'s id: ')
            quantity = int(input('Enter amount of components increased or decreased: '))
            print('Choose the update method')
            print('1. Receive components from suppliers')#part's quantity is increased
            print('2. Distribute components to section.')#part's quantity is decreased
            print('3. Create new parts')
            choice = int(input('Enter your option: '))
            if choice == 1:
               supplier = input('Enter supplier\'s company name: ')
               if warehouse.upper() == 'WBS':
                   increaseQuantity('bios_inventory.txt', identification, supplier, quantity)
               elif warehouse.upper() == 'WAY':
                    increaseQuantity('ambry_inventory.txt', identification, supplier, quantity)
               else:
                   increaseQuantity('barrier_inventory.txt', identification, supplier, quantity)                           
            elif choice == 2:
                print('1. Body work section (BWS)')
                print('2. Car engine section (CES)')
                print('3. Electronic section (ES)')
                print('4. Lighting section (LS)')
                print('5. Safety section (SS)')
                section = input('Enter one of the sections above: ')
                if warehouse.upper() == 'WBS':
                    decreaseQuantity('bios_inventory.txt', identification, section, quantity)
                elif warehouse.upper() == 'WAY':
                    decreaseQuantity('ambry_inventory.txt', identification, section, quantity)
                else:
                    decreaseQuantity('barrier_inventory.txt', identification, section, quantity)
            else:
                print('Invalid option')
"""This function asks the user to enter the update method, warehouse code, part id, amount updated etc.
for 30 to 50 percent of the parts available in each warehouse"""

def getPartDetails(file):
    try:
        fileHandler = open(file, 'r')
    except:
        print('File does not exist')
        exit()
    bigLst = []
    sectionLst = []
    nameLst = []
    idLst = []
    quantityLst = []
    priceLst = []
    materialLst = []
    supplierLst = []
    for line in fileHandler:
        newLine = line.strip().split('    ')
        sectionLst.append(newLine[0])
        nameLst.append(newLine[1])
        idLst.append(newLine[2])
        quantityLst.append(newLine[3])
        priceLst.append(newLine[4])
        materialLst.append(newLine[5])
        supplierLst.append(newLine[6])
    bigLst.append(sectionLst)
    bigLst.append(nameLst)
    bigLst.append(idLst)
    bigLst.append(quantityLst)
    bigLst.append(priceLst)
    bigLst.append(materialLst)
    bigLst.append(supplierLst)
    fileHandler.close()
    return bigLst
#This function stores each part's section, name, id, quantity, price, material and supplier's name in their respective lists
#These lists are then stored in one big list

def trackInventory():
    print('Choose the operation to track inventory: ')
    print('1.sort part id by ascending order and display quantity available')
    print('2.record parts with less than 10 units in warehouse')
    print('3.record parts and quantity for each assembly section')
    choice = int(input('Enter your option: '))
    systemData = []
    biosData = getPartDetails('bios_inventory.txt')#for Bios warehouse (WBS)
    ambryData = getPartDetails('ambry_inventory.txt')#for Ambry warehouse (WAY)
    barrierData = getPartDetails('barrier_inventory.txt')#for Barrier warehouse (WBR)
    systemData.append(biosData)
    systemData.append(ambryData)
    systemData.append(barrierData)
    if choice == 1:
        temp = []
        for warehouse in systemData:
            #warehouse[2] is the list with all part's id in it
            #warehouse[3] is the list with all part's quantity in it
            for i in range(len(warehouse[2])):
                temp.append(warehouse[2][i] + '    ' + warehouse[3][i])
        return sorted(temp)
    elif choice == 2:
        lst = []
        modelName = ['bios: ', 'ambry: ', 'barrier: ']
        for i in range(len(systemData)):
            smallLst = []
            for j in range(len(systemData[i][3])):
                #systemData[i][1] is the list with all part's name in it
                #systemData[i][2] is the list with all part's id in it
                #systemData[i][3] is the list with all part's quantity in it
                if int(systemData[i][3][j].split(': ')[1]) < 10:
                    smallLst.append(systemData[i][1][j] + '    ' + systemData[i][2][j] + '    ' + systemData[i][3][j])
            lst.append(modelName[i] + str(smallLst))
        return lst
    elif choice == 3:
        bigLst = []
        modelName = ['bios: ', 'ambry: ', 'barrier: ']
        for i in range(len(systemData)):
            tinyLst = []
            for j in range(len(systemData[i][3])):
                #systemData[i][0] is the list with all part's section number in it
                tinyLst.append(systemData[i][0][j] + '    ' + systemData[i][1][j] + '    ' + systemData[i][2][j] + '    ' + systemData[i][3][j])
            bigLst.append(modelName[i] + str(tinyLst))
        return bigLst
    else:
        print('Invalid option')
#This function prints the part's details accoring to the user's choice

def searchInventory():
    print('Choose the operation to search inventory: ')
    print('1.display part\'s record when searched by part\'s id')
    print('2.display supplier details when searched by part\'s id')
    print('3.display parts when searched by supplier\'s name')
    choice = int(input('Enter your option: '))
    systemData = []
    biosData = getPartDetails('bios_inventory.txt')#for Bios warehouse (WBS)
    ambryData = getPartDetails('ambry_inventory.txt')#for Ambry warehouse (WAY)
    barrierData = getPartDetails('barrier_inventory.txt')#for Barrier warehouse (WBR)
    systemData.append(biosData)
    systemData.append(ambryData)
    systemData.append(barrierData)
    if choice == 1:
        lst = []
        searchId = input('Please enter the part\'s id you want to search: ')#searched by part ID
        for warehouse in systemData:
            #warehouse[0] is the list with all part's section number in it
            #warehouse[1] is the list with all part's name in it
            #warehouse[2] is the list with all part's id in it
            #warehouse[3] is the list with all part's quantity in it
            #warehouse[4] is the list with all part's price in it
            #warehouse[5] is the list with all part's material in it
            #warehouse[6] is the list with all part's supplier's name in it
            for i in range(len(warehouse[2])):
                if warehouse[2][i].split(': ')[1].lower() == searchId.lower():
                    lst.append(warehouse[0][i])
                    lst.append(warehouse[1][i])
                    lst.append(warehouse[2][i])
                    lst.append(warehouse[3][i])
                    lst.append(warehouse[4][i])
                    lst.append(warehouse[5][i])
        return lst                                   
    elif choice == 2:
        temp = []
        searchId = input('Please enter the part\'s id you want to search: ')#searched by part ID
        for warehouse in systemData:
            for i in range(len(warehouse[2])):
                if warehouse[2][i].split(': ')[1].lower() == searchId.lower():
                    temp.append(warehouse[2][i])
                    temp.append(warehouse[6][i])
        return temp
    elif choice == 3:
        partsLst = []
        supplier = input('Please enter supplier\'s name: ')#searched by supplier's name
        for warehouse in systemData:
            for i in range(len(warehouse[6])):
                detailsLst = []
                if warehouse[6][i].split(': ')[1].lower() == supplier.lower():
                    detailsLst.append(warehouse[0][i])
                    detailsLst.append(warehouse[1][i])
                    detailsLst.append(warehouse[2][i])
                    detailsLst.append(warehouse[3][i])
                    detailsLst.append(warehouse[4][i])
                    detailsLst.append(warehouse[5][i])
                    detailsLst.append(warehouse[6][i])
                if detailsLst != []:
                    partsLst.append(detailsLst)
                #empty lists do not provide any details so they are not printed
        return partsLst
    else:
        print('Invalid option')
#This function searches for the relevant part's details based on the feature or criteria entered by the user

def addNewParts(file):
    try:
        fileHandler = open(file, 'a')
    except:
        print('File does not exist')
        exit()
    print('1. Body work section (BWS)')
    print('2. Car engine section (CES)')
    print('3. Electronic section (ES)')
    print('4. Lighting section (LS)')
    print('5. Safety section (SS)')
    partDetails = []
    section = 'section: ' + input('Enter one of the sections above: ')
    name = 'name: ' + input('Enter name of component: ')
    identification = 'id: ' + input('Enter "XX01" for first component, "XX02" for second component and so on: ')
    quantity = 'quantity: ' + input('Enter number of components available: ')
    price = 'price: RM' + input('Enter price of each component: ')
    material = 'material: ' + input('Enter material used to make the component: ')
    supplier = 'supplier: ' + input('Enter supplier\'s company name: ')
    partDetails.append(section)
    partDetails.append(name)
    partDetails.append(identification)
    partDetails.append(quantity)
    partDetails.append(price)
    partDetails.append(material)
    partDetails.append(supplier)
    for element in partDetails:
        if element.startswith('id: '):
            if file == 'bios_inventory.txt':
                element = element.replace('XX', 'BS')
            elif file == 'ambry_inventory.txt':
                element = element.replace('XX', 'AY')
            elif file == 'barrier_inventory.txt':
                element = element.replace('XX', 'BR')
            else:
                print('Invalid file name')
            
        fileHandler.write(element + '    ')
    fileHandler.write('\n')
    fileHandler.close()
#This function writes new part and its details into the corresponding text files

def menu():
    print('Welcome to the Automobile Parts Inventory Management System')
    print('Please select the operation you want to perform')
    print('1.save Bios inventory')
    print('2.save Ambry inventory')
    print('3.save Barrier inventory')
    print('4.count number of parts in each warehouse')
    print('5.update inventory')
    print('6.track inventory')
    print('7.search inventory')
    print('8.add new parts to warehouse')
    option = int(input('Enter your choice: '))
    if option == 1:
        output = saveBiosInventory()
    elif option == 2:
        output = saveAmbryInventory()
    elif option == 3:
        output = saveBarrierInventory()
    elif option == 4:
        fileName = input('Enter name of file: ')
        number = countFileLines(fileName)
        output = 'There are ' + str(number) + ' components in the warehouse'
    elif option == 5:
        output = updateInventory()
    elif option == 6:
        output = trackInventory()
    elif option == 7:
        output = searchInventory()
    elif option == 8:
        fileName = input('Enter name of file: ')
        output = addNewParts(fileName)
    else:
        return 'Invalid option'
    print(output)
#This function prompts the user for their choice of operation

menu()



            
