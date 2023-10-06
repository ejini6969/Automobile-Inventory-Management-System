# Automobile-Inventory-Management-System

I, as a Python programmer, had been recruited by the automobile manufacturing company to write a program for the Automobile Parts Inventory Management System. So, the system consists of three automobile models, namely Bios (BS), Ambry (AY) and Barrier (BR). Each model has its own division and within each division there is a specific warehouse which stores various components. The warehouse code for Bios, Ambry and Barrier are  WBS, WAY and WBR  respectively. Besides, there are a total of five sections in every division, namely the body work section (section 1), car engine section (section 2), electronic section (section 3), lighting section (section 4) and safety section (section 5) which perform specific manufacturing tasks. Each section is responsible for producing the corresponding components using limited raw materials such as steel, glass, rubber etc.

## Functionality

* List out the details of every components in terms of **price**, **quantity in storage***, **materials** etc
* Update each part’s details
    * Track the latest record of various parts
    * **Increase or decrease the quantity** of specific parts
    * **Sort** the part ID’s of three warehouses in ascending order
    * **Display** parts’ details with less than 10 units in each warehouse
    * **Print** the part and their quantities available respectively to the user’s console
* Search for specific functionalities based on the users’ requirements
  * Find the corresponding parts’ and suppliers’ details when searched by **part ID**
  * Find the parts’ details when searched by **suppliers**

## Assumptions

* Only one variant is produced under each model
* Each component has its own unique part ID which consists of the model code followed by two additional digits in sequential order
    * BR01 stands for the 1st component in the Barrier warehouse
    * BS65 stands for the 65th component in the Bios warehouse
    * AY99 stands for the 99th component in the Ambry warehouse
* Each part is supplied by exactly one supplier but a supplier can supply more than one part
* Each model must have at least three sections operating and must be responsible in manufacturing at least 5 components of an automobile
