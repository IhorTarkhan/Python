from lxml import etree

parser = etree.XMLParser(dtd_validation=True)
tree = etree.parse("sample.xml", parser)
print(tree)


if __name__ == "__main__":
    print("Hello World!")
