# file: ead_write.py
#

import xml.etree.ElementTree as ET
from unpack_variable import unpack

def generate_ead(file_name):

    ET.register_namespace('', "http://ead3.archivists.org/schema/")

    root = ET.Element("ead")

    # <control> A new element in EAD3 and the first of <ead>’s two required child elements. Replaces <eadheader> and
    # aligns more with EAC-CPF, a focus on data, and a focus on sources of information and standards used. <control>
    # is used for recording bibliographic and administrative information about an EAD. It must contain the following
    # elements: <recordid>, <filedesc>, <maintenanceagency>, <maintenancestatus> and <maintenancehistory>.
    m1 = ET.Element("control")
    root.append(m1)

    # <recordid> This is a new element in EAD3 that designates a unique identifier for the EAD file. The template
    # uses an optional @instanceurl attribute to record the URL of the EAD xml file.
    b1 = ET.SubElement(m1, "recordid")
    b1.text = recordid
    # b1.txt = xmldict['recordid']
    # assuming that xmldict = {'recordid': '216', 'unitcode': '2004-001', 'unittitle': 'Rush Reporter Collection, 1975 - 1999'}

    # <filedesc> A child element of <control> that records bibliographic information about an EAD file such as
    # description of the finding aid, author, title, subtitle, sponsor, edition, publisher, publishing series,
    # and related notes. It must include a <titlestmt>.
    b2 = ET.SubElement(m1, "filedesc")
    b2.text = filedesc

    # <maintenanceagency> A child element of <filedesc> that groups together information about the name of an encoded
    # finding aid and those responsible for its content. The template uses a required child element <titleproper> to
    # record the title of a finding aid or finding aid series.
    b3 = ET.SubElement(m1, "maintenanceagency")
    b3.text = maintenanceagency

    # <maintenancestatus> A child element of <control> that records the current version status of the EAD file. The
    # current status must always be recorded in the required attribute @value which is limited to revised, deleted,
    # new, deletedsplit, deletedmerged, deletedreplaced, cancelled, derived).
    b4 = ET.SubElement(m1, "maintenancestatus")
    b4.text = maintenancestatus

    # <maintenancehistory> A child element of <control> that records information about the institution or service
    # responsible for the creation, maintenance, and /or dissemination of the EAD file. This template uses an
    # optional attribute @countrycode that specifies a unique code for the country in which the materials being
    # described are held. The recommended source for country codes is the ISO 3166-1 Codes for the Representation of
    # Names of Countries, column Alpha-2. <maintenanceagency> must also include a child <agencyname> that records the
    # name of the institution or service. This template also uses an optional element <agencycode> that provides a
    # code for the institution or service responsible for the creation, maintenance, or dissemination of the EAD
    # file. For best practices, use the format of International Standard Identifier for Libraries and Related
    # Organizations (ISO 15511). The code is composed of a prefix, a dash, and an identifier. For specific codes,
    # see the Library of Congress’s code search.
    b5 = ET.SubElement(m1, "maintenancehistory")
    b5.text = maintenancehistory

    # <archdesc> One of only two child elements of <ead>. <archdesc> follows the <control> element and wraps together
    # all of the archival descriptive information in an EAD file. It includes elements describing the content,
    # context, extent, administrative and other supplemental information that facilitates the use of the materials
    # which are organized in hierarchical levels.
    #
    # It includes a required attribute @level which indicates the type of aggregation being described in the EAD file
    # and must include the following values: class, collection, file, fonds, item, otherlevel, recordgrp, series,
    # subfonds, subgrp, or subseries. <archdesc> must contain a required child <did>.
    m2 = ET.Element("archdesc")
    # Set attribute
    root.append(m2)

    # <did> A required child element of <archdesc> that binds together other elements and records information about
    # the material to be described in the EAD file. It may also occur within other wrapper elements like c, c01,
    # c02 ... c12.
    c1 = ET.SubElement(m2, "did")

    # <repository> An optional child element of <did> that records the name of the institution, person, or family
    # responsible for providing intellectual access to the materials being described. At least one of four name
    # elements (<persname>, <famname>, <corpname>, or <name>) is required if this is used. This template uses
    # <corpname> and the optional <address>. <corpname> is used to identify the organization responsible for the
    # materials.
    if None in [repository_persname, repository_famname, repository_corpname, repository_name]:
        pass
    else:
        d1 = ET.SubElement(c1, "repository")
        if repository_persname is None:
            pass
        else:
            e1 = ET.SubElement(d1, "persname")
            e1.text = repository_persname
            # The name of the organization is encoded within its required and repeatable child element <part>.
            # <address> is used to bind together multiple required <addressline> child elements that provide information
            # about the place where the repository is located and how it may be contacted.
        if repository_famname is None:
            pass
        else:
            e2 = ET.SubElement(d1, "famname")
            e2.text = repository_famname
            # The name of the organization is encoded within its required and repeatable child element <part>.
            # <address> is used to bind together multiple required <addressline> child elements that provide information
            # about the place where the repository is located and how it may be contacted.
        if repository_corpname is None:
            pass
        else:
            e3 = ET.SubElement(d1, "corpname")
            e3.text = repository_corpname
            # The name of the organization is encoded within its required and repeatable child element <part>.
            # <address> is used to bind together multiple required <addressline> child elements that provide information
            # about the place where the repository is located and how it may be contacted.
        if repository_name is None:
            pass
        else:
            e4 = ET.SubElement(d1, "name")
            e4.text = repository_name
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
    if None in [origination_persname, origination_famname, origination_corpname, origination_name]:
        pass
    else:
        d2 = ET.SubElement(c1, "origination")
        if origination_persname is None:
            pass
        else:
            e1 = ET.SubElement(d2, "persname")
            e1.text = origination_persname
            # When handling personal names, we chose to use <part> to its fullest logical extent per the Study Group on
            # Discovery's recommendations. We then provided an example of how @localtype could be used to handle definition
            # of each <part> element in a way that will aid in display, searching, and sorting.
        if origination_famname is None:
            pass
        else:
            e2 = ET.SubElement(d2, "famname")
            e2.text = origination_famname
            # When handling personal names, we chose to use <part> to its fullest logical extent per the Study Group on
            # Discovery's recommendations. We then provided an example of how @localtype could be used to handle definition
            # of each <part> element in a way that will aid in display, searching, and sorting.
        if origination_corpname is None:
            pass
        else:
            e3 = ET.SubElement(d2, "corpname")
            e3.text = origination_corpname
            # When handling personal names, we chose to use <part> to its fullest logical extent per the Study Group on
            # Discovery's recommendations. We then provided an example of how @localtype could be used to handle definition
            # of each <part> element in a way that will aid in display, searching, and sorting.
        if origination_name is None:
            pass
        else:
            e4 = ET.SubElement(d2, "name")
            e4.text = origination_name
            # When handling personal names, we chose to use <part> to its fullest logical extent per the Study Group on
            # Discovery's recommendations. We then provided an example of how @localtype could be used to handle definition
            # of each <part> element in a way that will aid in display, searching, and sorting.

    # <unittitle> An optional child element of <did> that records the specified title for the described materials. It
    # can be used at <archdesc> level and at the subordinate <c> levels.
    if unittitle is None:
        pass
    else:
        d3 = ET.SubElement(c1, "unittitle")
        d3.text = unittitle

    # <unitid> An optional child element of <did> that provides an identifier for the materials being described.
    if unitid is None:
        pass
    else:
        d4 = ET.SubElement(c1, "unitid")
        d4.text = unitid

    # <unitdatestructured> A new element in EAD3 and an optional child element of <did> that records
    # machine-processable dates of the materials being described. We opted to highlight the use of this new element,
    # in lieu of using <unitdate> with a @normal attribute (EAD3 supports the same general type of <unitdate>
    # encoding as EAD Version 2002). Our sample file uses an optional attribute @unitdatetype that identifies the
    # type of date expressed with possible values of bulk or inclusive. When <unitdatestructured> is used,
    # it must contain one and only one of the following: <daterange>, <dateset>, <datesingle>. The sample file uses
    # an optional child element <daterange> to bind together dates encoded with optional (but recommended) <fromdate>
    # and <todate> elements.
    if None in [daterange, dateset, datesingle]:
        pass
    else:
        d5 = ET.SubElement(c1, "unitdatestructured")
        if None in [fromdate, todate]:
            pass
        else:
            i1 = ET.SubElement(d5, "daterange")
            j1 = ET.SubElement(i1, "fromdate")
            j1.text = fromdate
            j2 = ET.SubElement(i1, "todate")
            j2.text = todate
        if dateset is None:
            pass
        else:
            i2 = ET.SubElement(d5, "dateset")
            i2.text = dateset
        if datesingle is None:
            pass
        else:
            i3 = ET.SubElement(d5, "datesingle")
            i3.text = datesingle
    # <physdescset>	A new element in EAD3 and an optional child element of <did> that can be used to group two or more
    # optional <physdecstructured> elements. <physdecstructured> element quantifies the physical or logical extent of
    # the materials being described.
    # It must include two required attributes @coverage and @physdescstructuredtype.
    if type(physdecstructured) is tuple:
        d6 = ET.SubElement(c1, "physdescset")
        for n in len(physdecstructured):
            unpack(physdecstructured[n])
    else:

        if None in [physdecstructured_coverage, physdecstructured_type]:
            pass
        else:
            d6 = ET.SubElement(c1, "physdescset")
            f1 = ET.SubElement(d6, "physdecstructured")
            # @coverage, with two possible values whole or part, specifies whether the description refers to the entire unit
            # or only a part of the materials.
            k1 = ET.SubElement(f1, "coverage")
            k1.text = physdecstructured_coverage
            # @physdescstructuredtype defines the type of amount being described with the following possible values:
            # carrier: Refers to the number of containers.
            # materialtype: Indicates the type and/or number of items.
            # spaceoccupied: Describes the linear, cubic, or other space occupied by the materials.
            # otherphysdescstructuredtype: May be chosen if none of the other values are appropriate
            k2 = ET.SubElement(f1, "physdescstructuredtype")
            # <physdescstructuredtype> must include two required children. <quantity> to indicate the number of units present
            # in <unittype> and <unittype> to indicate the type of unit being quantified such as boxes, linear feet,
            # cubic feet, etc.
            l1 = ET.SubElement(k2, physdescstructuredtype_coverage)
            l2 = ET.SubElement(k2, physdescstructuredtype_unittype)

    if None in [quantity, unittype]:
        pass
    else:
        d7 = ET.SubElement(c1, "physdescstructuredtype")

        # <quantity> indicates the number of units present in <unittype>
        if quantity is None:
            pass
        else:
            g1 = ET.SubElement(d7, "quantity")
            g1.text = quantity

        # <unittype> indicates the type of unit being quantified such as boxes, linear feet, cubic feet, etc.
        if unittype is None:
            pass
        else:
            g2 = ET.SubElement(d7, "unittype")
            g2.text = unittype

    # <langmaterial> An optional child element of <did> which identifies the languages and scripts represented in the
    # materials. This template uses a required child element <language> to record the language(s) of the EAD file or
    # of the materials being described. <language> also includes a strongly recommended attribute @langcode to record
    # the code of the language which should be taken from from ISO 639-1, ISO 639-2b, ISO 639-3, or another controlled
    # list.
    if language is None:
        pass
    else:
        if type(language) is list: # test the heck out of this
            # language = [eng, esp, ger]
            d8 = ET.SubElement(c1, "langmaterial")
            for n in len(language):
                unpack(language[n])
        else:
            # language = eng
            d8 = ET.SubElement(c1, "langmaterial")
            h1 = ET.SubElement(d8, "language")
            h1.text = language

    # <accessrestrict> An optional element that records information about the conditions that affect the availability
    # of the materials being described.
    if accessrestrict is None:
        pass
    else:
        d9 = ET.SubElement(c1, "accessrestrict")
        d9.text = accessrestrict

    # <userestrict>	An optional element that indicates any conditions that govern the use of the described materials.
    if userestrict is None:
        pass
    else:
        d10 = ET.SubElement(c1, "userestrict")
        d10.text = userestrict

    # <scopecontent> An optional element that may contain the information about the arrangement of the materials,
    # dates covered by the materials, significant organizations, individuals, events, places and subjects represented
    # by the materials.
    if scopecontent is None:
        pass
    else:
        d11 = ET.SubElement(c1, "scopecontent")
        d11.text = scopecontent

    tree = ET.ElementTree(root)

    with open(file_name, "wb") as files:
        tree.write(files, encoding="UTF-8", xml_declaration=True, method="xml", short_empty_elements=True)


if __name__ == "__main__":
    generate_ead('test.xml')
