---
title: Configuration for File Resource Type
description: JasperReports Server allows to configure validators for files uploaded in the repository.
---

# Configuration for File Resource Type

JasperReports Server allows to configure validators for files uploaded in the repository.

While adding a file resource, you can only upload the files that are defined in the JasperReports Server repository. Only a valid file type (file type defined in JasperReports Server) and its corresponding file extension for that file type can be uploaded.

For more information on the list of allowed file types, see [File Resource Types](../resources/file_resources.md).

To configure the file resource type:

1.  Open the configuration file `…/WEB-INF/flows/fileResourceBeans.xml` for editing.

2.  Locate the `whitelistFileExtRegexByType` in the following file.

    ``` xml
    <util:map id="whitelistFileExtRegexByType">
            <entry key="accessGrantSchema" value="(.*\.(xml))"/>
            <entry key="css" value="(.*\.(css))"/>
            <entry key="font" value="(.*\.(ttf))"/>
            <entry key="img" value="(.*\.(jpg|jpeg|gif|bmp|png))"/>
            <entry key="jar" value="(.*\.(jar))"/>
            <entry key="jrxml" value="(.*\.(jrxml))"/>
            <entry key="olapMondrianSchema" value="(.*\.(xml))"/>
            <entry key="prop" value="(.*\.(properties))"/>
            <entry key="jrtx" value="(.*\.(jrtx))"/>
            <entry key="xml" value="(.*\.(xml|agxml))"/>
            <entry key="config" value="(.*\.(config))"/>
            <entry key="cer" value="(.*\.(p12|pfx))"/>
            <entry key="contentResource" value="(.*\.(docx|doc|ppt|pptx|xls|xlsx|ods|odt|odp|pdf|rtf|html|txt|csv|json))"/>
            <entry key="secureFile" value="^.+$"/>
            <entry key="mongoDbSchema" value="(.*\.(json))"/>
            <entry key="key" value="(.*\.(key))"/>
            <entry key="pub" value="(.*\.(pub))"/>
            <entry key="ppk" value="(.*\.(ppk))"/>
        </util:map>
    ```

    This map contains JasperReports Server repository file types mapping to file extensions. For example, `contentResource` is a file type in the JasperReports Server repository that is used to describe generated report outputs and some data sources, like CSV and JSON. When you upload content resource, only files with these extensions are allowed. At the same time, you cannot upload `.json` or `.csv` files as CSS or config files. Therefore, ensure that the correct file extension is set for the file that is chosen to be uploaded to the JasperReports Server repository.

3.  Locate the `fileNameRegexp` property in the same file.

    ``` xml
    <property name="fileNameRegexp" value="(.*\.(docx|doc|ppt|pptx|xls|xlsx|ods|odt|odp|pdf|rtf|html|txt|csv|json|xml|agxml|css|ttf|jpg|jpeg|gif|bmp|png|jrxml|jrtx|properties|config|p12|pfx|key|pub|ppk|jar))"/>
    ```

    The `fileNameRegexp` is a regular expression rule that defines the list of file extensions allowed to be uploaded. When uploading a file, first, this validation check has to pass, and then the next check is performed to verify if the file matches the corresponding file extension present in the `map: whitelistFileExtRegexByType`.

    If the file extension does not match the allowed file types, then an error message is returned.
