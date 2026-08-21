---
title: Disabling Open In Editor Option
description: "By default, the Open In Editor property is enabled. It appears on the context menu when you right-click the report or files in the repository. Using the Open In Editor option, you can edit the files..."
---

# Disabling Open In Editor Option

By default, the Open In Editor property is enabled. It appears on the context menu when you right-click the report or files in the repository. Using the Open In Editor option, you can edit the files including CSS, XML, JSON, and JRXML in the text editor and JRXML editor respectively. You can disable Open In Editor and hide it from the context menu by editing `…/WEB-INF/applicationContext-search.xml` file.

To disable the open in editor

1.  Open the file `…/WEB-INF/applicationContext-search.xml` file for editing.
2.  Locate the `searchActionModel` bean.
3.  Set the `openInEditor` property to false and save the file.

``` xml
<bean id="searchActionModel" class="com.jaspersoft.jasperserver.search.model.SearchActionModelSupport">
  <propertyname="proVersion"value="${isProVersion}"/>
  <propertyname="openInEditor"value="false"/>
</bean>
```

4.  Restart JasperReports Server.
