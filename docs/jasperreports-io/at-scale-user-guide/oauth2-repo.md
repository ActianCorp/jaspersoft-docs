---
title: OAuth2 Repositories
description: "By default, JasperReports IO At-Scale comes with three preconfigured OAuth2 repositories for Google Drive, GitHub, and Dropbox. Each of these is defined in the following folders:"
---

# OAuth2 Repositories

By default, JasperReports IO At-Scale comes with three preconfigured OAuth2 repositories for Google Drive, GitHub, and Dropbox. Each of these is defined in the following folders:

-   `jrio-export-docker/jrio/applicationContext-google-drive.xml`

-   `jrio-export-docker/jrio/applicationContext-github.xml`

-   `jrio-export-docker/jrio/applicationContext-dropbox.xml`

-   `jrio-reporting-docker/jrio/applicationContext-google-drive.xml`

-   `jrio-reporting-docker/jrio/applicationContext-github.xml`

-   `jrio-reporting-docker/jrio/applicationContext-dropbox.xml`

-   `jrio-rest-docker/jrio/WEB-INF/applicationContext-google-drive.xml`

-   `jrio-rest-docker/jrio/WEB-INF/applicationContext-github.xml`

-   `jrio-rest-docker/jrio/WEB-INF/applicationContext-dropbox.xml`

To use these repositories, each repository configuration file needs to be updated with actual `clientId` and `secretKey` values. These values are obtained from the target cloud storage providers while registering your JasperReports IO At-Scale instance with them.

The configuration file for the Google Drive repository appears similar to the following:

``` xml
<bean class="com.jaspersoft.jrio.common.repository.google.GoogleDriveRepositoryService">
   <property name="jasperReportsContext" ref="baseJasperReportsContext"/>
   <property name="googleDriveProvider">
      <bean class="com.jaspersoft.jrio.common.repository.google.RequestTokenGoogleDriveProvider">
         <property name="googleDriveFactory">
            <bean class="com.jaspersoft.jrio.common.repository.google.GoogleDriveFactory">
               <property name="clientId" value="put-client-id-here"/>
               <property name="secretKey" value="put-secret-key-here"/>
             </bean>
         </property>
         <property name="serviceCache">
            <bean class="com.jaspersoft.jrio.common.execution.cache.LocalCacheAccessFactory">
               <property name="cacheContainer" ref="localCacheManager"/>
               <property name="cacheRegion" value="googleDriveServices"/>
            </bean>
         </property>
       </bean>
    </property>
</bean>
```
