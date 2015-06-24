import xml.etree.ElementTree as xml

items = xml.parse('items.xml')
root = items.getroot()

print "Armours\n"

for armour in root.findall("armours"):
	for lightarmour in armour.findall("lightarmours"):
		name = lightarmour.find("name").text
		armor = lightarmour.find("armor").text
		print ("The %s gives %s armor" % (name, armor)) 

	for heavyarmour in armour.findall("heavyarmours"):
		name = heavyarmour.find("name").text
		armor = heavyarmour.find("armor").text
		print ("The %s gives %s armor" % (name, armor))
		 
	for midarmour in armour.findall("midarmours"):
		name = midarmour.find("name").text
		armor = midarmour.find("armor").text
		print ("The %s gives %s armor" % (name, armor))
		
	for helmet in armour.findall("helmets"):
		name = helmet.find("name").text
		armor = helmet.find("armor").text
		print ("The %s gives %s armor" % (name, armor))
		
	for boot in armour.findall("boots"):
		name = boot.find("name").text
		armor = boot.find("armor").text
		print ("The %s gives %s armor" % (name, armor))
		
	for glove in armour.findall("gloves"):
		name = glove.find("name").text
		armor = glove.find("armor").text
		print ("The %s gives %s armor" % (name, armor))
		
	for cloack in armour.findall("cloacks"):
		name = cloack.find("name").text
		armor = cloack.find("armor").text
		print ("The %s gives %s armor" % (name, armor))

print"\nAccesories\n"

for accesory in root.findall("accesories"):
	for ring in accesory.findall("rings"):
		name = ring.find("name").text
		armor = ring.find("armor").text
		print ("The %s gives %s armor" % (name, armor))

	for trinket in accesory.findall("trinkets"):
		name = trinket.find("name").text
		armor = trinket.find("armor").text
		print ("The %s gives %s armor" % (name, armor)) 

print"\nWeapons\n"

for weapon in root.findall("weapons"):
	for sword in weapon.findall("swords"):
		name = sword.find("name").text
		mindmg = sword.find("mindamage").text
		maxdmg = sword.find("maxdamage").text
		speed = sword.find("speed").text
		print ("The %s deals %s to %s damage at %s attacks per second" % (name, mindmg, maxdmg, speed)) 
		
	for axe in weapon.findall("axes"):
		name = axe.find("name").text
		mindmg = axe.find("mindamage").text
		maxdmg = axe.find("maxdamage").text
		speed = axe.find("speed").text
		print ("The %s deals %s to %s damage at %s attacks per second" % (name, mindmg, maxdmg, speed)) 

	for spear in weapon.findall("spears"):
		name = spear.find("name").text
		mindmg = spear.find("mindamage").text
		maxdmg = spear.find("maxdamage").text
		speed = spear.find("speed").text
		print ("The %s deals %s to %s damage at %s attacks per second" % (name, mindmg, maxdmg, speed)) 

	for fist in weapon.findall("fists"):
		name = fist.find("name").text
		mindmg = fist.find("mindamage").text
		maxdmg = fist.find("maxdamage").text
		speed = fist.find("speed").text
		print ("The %s deals %s to %s damage at %s attacks per second" % (name, mindmg, maxdmg, speed)) 
