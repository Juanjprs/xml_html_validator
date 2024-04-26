import xml.etree.ElementTree as ET

def validar_xml(xml_file, xsd_file):
    # Carrega o arquivo XML
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Carrega o arquivo XSD (XML Schema)
    with open(xsd_file, 'r') as f:
        xsd_content = f.read()

    # Verifica se as tags do XML correspondem ao XSD
    errors = []
    for elem in root.iter():
        if '}' in elem.tag:
            tag = elem.tag.split('}')[1]
        else:
            tag = elem.tag
        if tag not in xsd_content:
            errors.append(f"Tag '{tag}' não está presente no XSD.")

    if errors:
        print("\nO XML é inválido de acordo com o XML Schema fornecido:")
        for error in errors:
            print(error)

    if errors:
        exit()

    # Extrai a ordem dos elementos do XSD
    xsd_order = []
    for line in xsd_content.splitlines():
        if '<xs:element' in line:
            element_name = line.split('name="')[1].split('"')[0]
            xsd_order.append(element_name)

    
    # Verificar a ordem dos elementos no XML em relação ao XSD
    errorsOrdem = []
    xml_order = [elem.tag.split('}')[-1] for elem in root.iter()]
    for i, (elem_xsd, elem_xml) in enumerate(zip(xsd_order, xml_order)):
        if elem_xsd != elem_xml:
            errorsOrdem.append(f"{elem_xml}")

    if errorsOrdem:
        print("\nO XML não está na ordem correta de acordo com o XML Schema fornecido. Corrija os elementos",errorsOrdem)

    

    # Extrair todas as tags definidas no XSD
    xsd_tags = set()
    for line in xsd_content.splitlines():
        if '<xs:element' in line:
            element_name = line.split('name="')[1].split('"')[0]
            xsd_tags.add(element_name)

    # Extrair todas as tags presentes no XML
    xml_tags = set()
    for elem in root.iter():
        if '}' in elem.tag:
            tag = elem.tag.split('}')[1]
        else:
            tag = elem.tag
        xml_tags.add(tag)

    # Verificar se todas as tags definidas no XSD estão presentes no XML
    unused_tags = xsd_tags - xml_tags
    if unused_tags:
        print("\nAs seguintes tags definidas no XSD não estão sendo usadas no XML:")
        for tag in unused_tags:
            print(tag)
    else:
        if len(errorsOrdem) == 0 and len(errors) == 0:
            print("\nO XML é válido de acordo com o XML Schema fornecido.")

# Arquivo XML a ser validado
xml_file = "testeX.xml"

# Arquivo XSD (XML Schema) para validação
xsd_file = "XMLSchema.xsd"

# Chamada da função de validação
validar_xml(xml_file, xsd_file)