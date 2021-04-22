# ead_write.py
#


import xml.etree.ElementTree as ET


def generate_ead(file_name):

    # record_object = populate_record_object(open(input('Please enter the name of a DB/TextWorks XML file to convert: ')))
    # This is a test record_id dict
    record_object = {'recordid': 'recordid',
                     'filedesc': 'filedesc',
                     'maintenanceagency': 'maintenanceagency',
                     'maintenancestatus': 'maintenancestatus',
                     'maintenancehistory': 'maintenancehistory',
                     'repository': 'repository-test',
                     'repository_persname': 'repository_persname',
                     'repository_famname': 'repository_famname',
                     'repository_corpname': 'repository_corpname',
                     'repository_name': 'repository_name',
                     'origination_persname': 'origination_persname',
                     'origination_famname': 'origination_famname',
                     'origination_corpname': 'origination_corpname',
                     'origination_name': 'origination_name',
                     'unittile': 'unittile',
                     'unitid': 'unitid',
                     'unitdatestructured': 'unitdatestructured',
                     'daterange': 'daterange',
                     'dateset': 'dateset',
                     'fromdate': 'fromdate',
                     'todate': 'todate',
                     'datesingle': 'datesingle',
                     'physdecstructured': 'physdecstructured',
                     'physdecstructured_coverage': 'physdecstructured_coverage',
                     'physdecstructured_type': 'physdecstructured_type',
                     'physdescstructuredtype_coverage': 'physdescstructuredtype_coverage',
                     'physdescstructuredtype_unittype': 'physdescstructuredtype_unittype',
                     'quantity': 'quantity',
                     'unittype': 'unittype',
                     'langmaterial': 'langmaterial',
                     # 'language': 'language',
                     'language': ['en', 'es', 'it'],
                     'accessrestrict': 'accessrestrict',
                     'userestrict': 'userestrict',
                     'scopecontent': 'scopecontent',
                     'maintenancehistory_attr_countrycode': 'maintenancehistory_attr_countrycode'}

    # Namespace
    ET.register_namespace('ead', 'http://ead3.archivists.org/schema/')

    # Establish <ead> as root element
    root = ET.Element('ead')

    # Create and populate <control>
    control_element = ET.Element('control')
    root.append(control_element)
    recordid_element = ET.SubElement(control_element, 'recordid')
    recordid_element.text = record_object.get('recordid')
    filedesc_element = ET.SubElement(control_element, 'filedesc')
    filedesc_element.text = record_object.get('filedesc')
    maintenanceagency_element = ET.SubElement(control_element, 'maintenanceagency')
    maintenanceagency_element.text = record_object.get('maintenanceagency')
    maintenancestatus_element = ET.SubElement(control_element, 'maintenancestatus')
    maintenancestatus_element.text = record_object.get('maintenancestatus')
    maintenancehistory_element = ET.SubElement(control_element, 'maintenancehistory')
    maintenancehistory_element.text = record_object.get('maintenancehistory')
    if record_object.get('maintenancehistory_attr_countrycode') is None:
        pass
    else:
        maintenancehistory_element.set('countrycode', record_object.get('maintenancehistory_attr_countrycode'))
    archdesc_element = ET.Element('archdesc')
    root.append(archdesc_element)

    # Create and populate <did> element
    # Populate did element
    # <did> A required child element of <archdesc> that binds together other elements and records information about
    # the material to be described in the EAD file. It may also occur within other wrapper elements like c, c01,
    # c02 ... c12.
    did_element = ET.SubElement(archdesc_element, 'did')

    # <repository> An optional child element of <did> that records the name of the institution, person, or family
    # responsible for providing intellectual access to the materials being described. At least one of four name
    # elements (<persname>, <famname>, <corpname>, or <name>) is required if this is used. This template uses
    # <corpname> and the optional <address>. <corpname> is used to identify the organization responsible for the
    # materials.
    if None in [record_object.get('repository_persname'),
                record_object.get('repository_famname'),
                record_object.get('repository_corpname'),
                record_object.get('repository_name')
                ]:
        pass
    else:
        repository_element = ET.SubElement(did_element, 'repository')
        if record_object.get('repository_persname') is None:
            pass
        else:
            repository_persname_element = ET.SubElement(repository_element, 'persname')
            repository_persname_element.text = record_object.get('repository_persname')
            # The name of the organization is encoded within its required and repeatable child element <part>.
            # <address> is used to bind together multiple required <addressline> child elements that provide information
            # about the place where the repository is located and how it may be contacted.
        if record_object.get('repository_famname') is None:
            pass
        else:
            repository_famname_element = ET.SubElement(repository_element, 'famname')
            repository_famname_element.text = record_object.get('repository_famname')
            # The name of the organization is encoded within its required and repeatable child element <part>.
            # <address> is used to bind together multiple required <addressline> child elements that provide information
            # about the place where the repository is located and how it may be contacted.
        if record_object.get('repository_corpname') is None:
            pass
        else:
            repository_corpname_element = ET.SubElement(repository_element, 'corpname')
            repository_corpname_element.text = record_object.get('repository_corpname')
            # The name of the organization is encoded within its required and repeatable child element <part>.
            # <address> is used to bind together multiple required <addressline> child elements that provide information
            # about the place where the repository is located and how it may be contacted.
        if record_object.get('repository_name') is None:
            pass
        else:
            repository_name_element = ET.SubElement(repository_element, 'name')
            repository_name_element.text = record_object.get('repository_name')
            # The name of the organization is encoded within its required and repeatable child element <part>.
            # <address> is used to bind together multiple required <addressline> child elements that provide information
            # about the place where the repository is located and how it may be contacted.

    # <origination> An optional child element of <did> that specifies the name of an individual, organization,
    # or family responsible for the described materials. At least one of four name elements (<persname>, <famname>,
    # <corpname>, or <name>) is required if this is used. This template uses the child element <persname> to identify
    # the personal name of the collector which is encoded within its required and repeatable child element <part>.
    # While @localtype's values are not standardized, developing standards for similar types of information across
    # consortia could aid in aggregate parsing of EAD finding aids. The experimental element may also satisfy DACS 2.6,
    # but as it is designated as experimental, we chose to recommend use of <origination>.
    if None in [record_object.get('origination_persname'),
                record_object.get('origination_famname'),
                record_object.get('origination_corpname'),
                record_object.get('origination_name')]:
        pass
    else:
        origination_element = ET.SubElement(did_element, 'origination')
        if record_object.get('origination_persname') is None:
            pass
        else:
            origination_persname_element = ET.SubElement(origination_element, 'persname')
            origination_persname_element.text = record_object.get('origination_persname')
            # When handling personal names, we chose to use <part> to its fullest logical extent per the Study Group on
            # Discovery's recommendations. We then provided an example of how @localtype could be used to handle definition
            # of each <part> element in a way that will aid in display, searching, and sorting.
        if record_object.get('origination_famname') is None:
            pass
        else:
            origination_famname_element = ET.SubElement(origination_element, 'famname')
            origination_famname_element.text = record_object.get('origination_famname')
            # When handling personal names, we chose to use <part> to its fullest logical extent per the Study Group on
            # Discovery's recommendations. We then provided an example of how @localtype could be used to handle definition
            # of each <part> element in a way that will aid in display, searching, and sorting.
        if record_object.get('origination_corpname') is None:
            pass
        else:
            origination_corpname_element = ET.SubElement(origination_element, 'corpname')
            origination_corpname_element.text = record_object.get('origination_corpname')
            # When handling personal names, we chose to use <part> to its fullest logical extent per the Study Group on
            # Discovery's recommendations. We then provided an example of how @localtype could be used to handle definition
            # of each <part> element in a way that will aid in display, searching, and sorting.
        if record_object.get('origination_name') is None:
            pass
        else:
            origination_name_element = ET.SubElement(origination_element, 'name')
            origination_name_element.text = record_object.get('origination_name')
            # When handling personal names, we chose to use <part> to its fullest logical extent per the Study Group on
            # Discovery's recommendations. We then provided an example of how @localtype could be used to handle definition
            # of each <part> element in a way that will aid in display, searching, and sorting.

    # <unittitle> An optional child element of <did> that records the specified title for the described materials. It
    # can be used at <archdesc> level and at the subordinate <c> levels.
    if record_object.get('unittitle') is None:
        pass
    else:
        unittitle_element = ET.SubElement(did_element, 'unittitle')
        unittitle_element.text = record_object.get('unittitle')

    # <unitid> An optional child element of <did> that provides an identifier for the materials being described.
    if record_object.get('unitid') is None:
        pass
    else:
        unitid_element = ET.SubElement(did_element, 'unitid')
        unitid_element.text = record_object.get('unitid')

    # <unitdatestructured> A new element in EAD3 and an optional child element of <did> that records
    # machine-processable dates of the materials being described. We opted to highlight the use of this new element,
    # in lieu of using <unitdate> with a @normal attribute (EAD3 supports the same general type of <unitdate>
    # encoding as EAD Version 2002). Our sample file uses an optional attribute @unitdatetype that identifies the
    # type of date expressed with possible values of bulk or inclusive. When <unitdatestructured> is used,
    # it must contain one and only one of the following: <daterange>, <dateset>, <datesingle>. The sample file uses
    # an optional child element <daterange> to bind together dates encoded with optional (but recommended) <fromdate>
    # and <todate> elements.
    if None in [record_object.get('daterange'),
                record_object.get('dateset'),
                record_object.get('datesingle')]:
        pass
    else:
        unitdatestructured_element = ET.SubElement(did_element, 'unitdatestructured')
        if None in [record_object.get('fromdate'),
                    record_object.get('todate')]:
            pass
        else:
            daterange_element = ET.SubElement(unitdatestructured_element, 'daterange')
            fromdate_element = ET.SubElement(daterange_element, 'fromdate')
            fromdate_element.text = record_object.get('fromdate')
            todate_element = ET.SubElement(daterange_element, 'todate')
            todate_element.text = record_object.get('todate')
        if record_object.get('dateset') is None:
            pass
        else:
            dateset_element = ET.SubElement(unitdatestructured_element, 'dateset')
            dateset_element.text = record_object.get('dateset')
        if record_object.get('datesingle') is None:
            pass
        else:
            datesingle_element = ET.SubElement(unitdatestructured_element, 'datesingle')
            datesingle_element.text = record_object.get('datesingle')
    # <physdescset>	A new element in EAD3 and an optional child element of <did> that can be used to group two or more
    # optional <physdecstructured> elements. <physdecstructured> element quantifies the physical or logical extent of
    # the materials being described.
    # It must include two required attributes @coverage and @physdescstructuredtype.
        if type(record_object.get('physdecstructured')) is list:
            physdescset_element = ET.SubElement(did_element, 'physdescset')
            for pds in range(len(record_object.get('physdecstructured'))):
                physdecstructured_element = ET.SubElement(physdescset_element, 'physdecstructured')
                physdecstructured_element.text = str(record_object.get('physdecstructured')[pds])
        else:
            if None in [record_object.get('physdecstructured_coverage'),
                        record_object.get('physdecstructured_type')]:
                pass
            else:
                # I believe this case should never happen, as the physdescset is intended to hold *two or more* physdecstructured
                # elements, but this is here as a bailout
                physdescset_element = ET.SubElement(did_element, 'physdescset')
                physdecstructured_element = ET.SubElement(physdescset_element, 'physdecstructured')
                # @coverage, with two possible values whole or part, specifies whether the description refers to the entire unit
                # or only a part of the materials.
                coverage_element = ET.SubElement(physdecstructured_element, 'coverage')
                coverage_element.text = record_object.get('physdecstructured_coverage')
                # @physdescstructuredtype defines the type of amount being described with the following possible values:
                # carrier: Refers to the number of containers.
                # materialtype: Indicates the type and/or number of items.
                # spaceoccupied: Describes the linear, cubic, or other space occupied by the materials.
                # otherphysdescstructuredtype: May be chosen if none of the other values are appropriate
                physdescstructuredtype_element = ET.SubElement(physdecstructured_element, 'physdescstructuredtype')
                # <physdescstructuredtype> must include two required children. <quantity> to indicate the number of units present
                # in <unittype> and <unittype> to indicate the type of unit being quantified such as boxes, linear feet,
                # cubic feet, etc.
                physdescstructuredtype_quantity_element = ET.SubElement(physdescstructuredtype_element, 'quantity')
                physdescstructuredtype_quantity_element.text = record_object.get('physdecstructuredtype_quantity')
                physdescstructuredtype_unittype_element = ET.SubElement(physdescstructuredtype_element, 'unittype')
                physdescstructuredtype_unittype_element.text = record_object.get('physdecstructuredtype_unittype')
    if None in [record_object.get('quantity'),
                record_object.get('unittype')]:
        pass
    else:
        physdescstructuredtype_element = ET.SubElement(did_element, 'physdescstructuredtype')
        # <quantity> indicates the number of units present in <unittype>
        if record_object.get('quantity') is None:
            pass
        else:
            physdescsetstructuredtype_quantity_element = ET.SubElement(physdescstructuredtype_element, 'quantity')
            physdescsetstructuredtype_quantity_element.text = record_object.get('quantity')
        # <unittype> indicates the type of unit being quantified such as boxes, linear feet, cubic feet, etc.
        if record_object.get('unittype') is None:
            pass
        else:
            physdescsetstructuredtype_quantity_unittype = ET.SubElement(physdescstructuredtype_element, 'unittype')
            physdescsetstructuredtype_quantity_unittype.text = record_object.get('unittype')

    # <langmaterial> An optional child element of <did> which identifies the languages and scripts represented in the
    # materials. This template uses a required child element <language> to record the language(s) of the EAD file or
    # of the materials being described. <language> also includes a strongly recommended attribute @langcode to record
    # the code of the language which should be taken from from ISO 639-1, ISO 639-2b, ISO 639-3, or another controlled
    # list.
    if record_object.get('language') is None:
        pass
    else:
        if type(record_object.get('language')) is list:
            langmaterial_element = ET.SubElement(did_element, 'langmaterial')
            for lang in range(len(record_object.get('language'))):
                language_element = ET.SubElement(langmaterial_element, 'language')
                language_element.text = str(record_object.get('language')[lang])
        else:
            langmaterial_element = ET.SubElement(did_element, 'langmaterial')
            language_element = ET.SubElement(langmaterial_element, 'language')
            language_element.text = record_object.get('language')

    # <accessrestrict> An optional element that records information about the conditions that affect the availability
    # of the materials being described.
    if record_object.get('accessrestrict') is None:
        pass
    else:
        accessrestrict_element = ET.SubElement(did_element, 'accessrestrict')
        accessrestrict_element.text = record_object.get('accessrestrict')

    # <userestrict>	An optional element that indicates any conditions that govern the use of the described materials.
    if record_object.get('userestrict') is None:
        pass
    else:
        userestrict_element = ET.SubElement(did_element, 'userestrict')
        userestrict_element.text = record_object.get('userestrict')

    # <scopecontent> An optional element that may contain the information about the arrangement of the materials,
    # dates covered by the materials, significant organizations, individuals, events, places and subjects represented
    # by the materials.
    if record_object.get('scopecontent') is None:
        pass
    else:
        scopecontent_element = ET.SubElement(did_element, 'scopecontent')
        scopecontent_element.text = record_object.get('scopecontent')

    tree = ET.ElementTree(root)

    with open(file_name, 'wb') as files:
        tree.write(files, encoding='UTF-8', xml_declaration=True, method='xml', short_empty_elements=True)


if __name__ == '__main__':
    generate_ead('test.xml')
