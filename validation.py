from lxml import etree

def validate():
    result1,result2 = 0,0
    xsd_doc = etree.parse("user_data.xsd")
    xmlschema = etree.XMLSchema(xsd_doc)
    # parse xml
    try:
        doc = etree.parse("user_data.xml")
        print('XML well formed, syntax ok.')
        result1= 1

    # check for file IO error
    except IOError:
        print('Invalid File')

    # check for XML syntax errors
    except etree.XMLSyntaxError as err:
        print('XML Syntax Error, see error_syntax.log')
        with open('error_syntax.log', 'w') as error_log_file:
            error_log_file.write(str(err.error_log))
        quit()

    except:
        print('Unknown error, exiting.')
        quit()

    # validate against schema
    try:
        xmlschema.assertValid(doc)
        print('XML valid, schema validation ok.')
        result2=1

    except etree.DocumentInvalid as err:
        print('Schema validation error, see error_schema.log')
        with open('error_schema.log', 'w') as error_log_file:
            error_log_file.write(str(err.error_log))
        quit()

    except:
        print('Unknown error, exiting.')
        quit()

    return result1,result2

