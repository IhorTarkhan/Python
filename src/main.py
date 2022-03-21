from xml.dom.minidom import Document
from xml.dom.minidom import Element

# Створюємо кореневий елемент
root: Document = Document()
xml: Element = root.createElement('map')
root.appendChild(xml)
# Створюємо об'єкт "країна"
country1: Element = root.createElement("country")
country1.setAttribute("id", "1")
country1.setAttribute("name", "Україна")
xml.appendChild(country1)
# Створюємо ще один об'єкт "країна"
country2 = root.createElement("country")
country2.setAttribute("id", "2")
country2.setAttribute("name", "Білорусь")
xml.appendChild(country2)
# Створюємо об'єкти "міста"
city1 = root.createElement("city")
city1.setAttribute("id", "1")
city1.setAttribute("name", "Київ")
city1.setAttribute("count", "3000000")
city1.setAttribute("iscap", "1")
xml.appendChild(city1)
city2 = root.createElement("city")
city2.setAttribute("id", "5")
city2.setAttribute("name", "Вітебськ")
city2.setAttribute("count", "350000")
city2.setAttribute("iscap", "0")
xml.appendChild(city2)

xml_str = root.toxml()
save_path_file = "countries.xml"
with open(save_path_file, "w") as f:
    f.write(xml_str)

import xml
from xml.dom.minidom import Document, Element

save_path_file = "countries.xml"
with xml.dom.minidom.parse(save_path_file) as dom:
    dom2: Document = dom
    mapElement: Element = dom2.getElementsByTagName("map")[0]
    print(mapElement.getAttribute("id"))
    lis = mapElement.childNodes
    for node in lis:
        # print(type(node))
        # node: Element = node
        # print(node.getAttribute("id"))
        if node.nodeType == node.ELEMENT_NODE:
            node: Element = node
            print(node.tagName + " " + node.getAttribute("id"))
