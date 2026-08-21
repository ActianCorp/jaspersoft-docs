---
title: Repository API
description: It’s easy to populate the repository (using metadata or output content) and subsequently exploit it. This functionality relies on a limited set of interfaces and classes.
---

# Repository API

It’s easy to populate the repository (using metadata or output content) and subsequently exploit it. This functionality relies on a limited set of interfaces and classes.

## Object Model and Service

The `com.jaspersoft.jasperserver.api.metadata.common.service.RepositoryService` interface is central to accessing the metadata repository. It exposes various methods to store, look up, and retrieve content from the repository. The repository is hierarchical and very similar to a file system. However, instead of files, the repository stores resources in a metadata representation of a tree structure.

All resources must have a name, label (display name), description, and type. Names must be unique within a folder. Resources reference their parent folder and are uniquely identified by their absolute URI. This URI consists of the full folder path within the repository, suffixed with the resource name. For example, the URI for the ContentFiles folder created when you run the installer is /ContentFiles.

From the object model perspective, all resources are instances of the `com.jaspersoft.jasperserver.api.metadata.common.domain.Resource`<br>
interface and represent various entities that constitute the metadata (such as reports, data sources, datatypes, analysis views, and fonts), or generated content (such as generated report output in PDF or XLS format).

Even folders are special types of resources. The `com.jaspersoft.jasperserver.api.metadata.common.domain.Folder`<br>
interface, which represents folders, directly inherits from `com.jaspersoft.jasperserver.api.metadata.common.domain.Resource` .

All interfaces that represent the main object model of the repository have convenience class implementations in the `com.jaspersoft.jasperserver.api.metadata.common.domain.client` package. They have the `Impl` suffix added to their corresponding interface name. These implementations are shown in the examples that follow when you instantiate folders and resources.

## Working with Folders

With the most minimal setup (manual WAR file deployment), the repository includes a single folder by default. It serves as the repository’s root directory. In this setup, we recommend that you create sensible folders (within root) to hold all your repository resources.

If you use one of the installers, the root directory includes a number of standard folders. You can use them as-is or create your own structure, depending on your needs. The following code creates a folder in /root:

``` text
import com.jaspersoft.jasperserver.api.common.domain.ExecutionContext;
import com.jaspersoft.jasperserver.api.metadata.common.service.RepositoryService;
import com.jaspersoft.jasperserver.api.metadata.common.domain.client.FolderImpl;
...
ExecutionContext context = ...; // gets the instance of the ExecutionContext
                                // interface, or receives it as a parameter in the
                                // current method
RepositoryService repositoryService = ...; // gets the instance of the
                                           // RepositoryService interface
...
Folder myFolder = new FolderImpl();
myFolder.setName("examples");
myFolder.setLabel("Examples");
myFolder.setDescription("Folder containing various resources to use as examples.");
repositoryService.saveFolder(context, myFolder);
```

Note that the code doesn’t specify a parent for the new folder. In this case, the server assumes that the new resource should reside in /root.

The following code creates a new subfolder in the /examples folder created immediately above:

``` text
Folder imagesFolder = new FolderImpl();
imagesFolder.setName("images");
imagesFolder.setLabel("Images");
imagesFolder.setDescription("Folder containing image resources to use in the examples.");
imagesFolder.setParentFolder("/examples");
repositoryService.saveFolder(context, imagesFolder);
```

The following code gets the /examples/images subfolder and changes its description:

``` text
Folder imagesFolder = repositoryService.getFolder(context, "/examples/images");
imagesFolder.setDescription("Example Images Folder");
repositoryService.saveFolder(context, imagesFolder);
```

The existence of a folder can be verified using the `folderExists` method, as shown here:

``` text
repositoryService.folderExists(context, "/examples/images");
```

Removing a folder from the repository is also easy. It needs only one method call that identifies the folder by its absolute URI. For example:

``` text
repositoryService.deleteFolder(context, "/examples/images");
```

Just as the server’s web interface lets you explore the repository and manage it, the API includes methods (exposed by the RepositoryService) that allow you to get a list of subfolders and manage a given folder’s content. The API includes one method that gets the list of subfolders and another method that gets the list of other types of child resources. For example, the following code returns a list of folders:

``` text
List folders = repositoryService.getSubFolders(context, "/reports"); if (folders.isEmpty()) {
  System.out.println("No folders found under /reports"); } else {
  System.out.println(folders.size() + " folder(s) found under /reports");
  for (Iterator it = folders.iterator(); it.hasNext();) {
    Folder folder = (Folder) it.next();
    System.out.println("Subfolder: " + folder.getName());
  }
}
```

## Repository Resources

Adding a other new resource in the repository differs from adding a folder. Unlike folders, which are simple in structure and behavior, other types of resources might need to be initialized in a special way, and the initialization logic would probably reside in a service. As a result, we created a unique API for managing repository resources. You can use it regardless of type and internal structure.

You create new resource instances by making a special request to the `RepositoryService`, not by direct instantiation. See the following example where you create a new image resource and load it to the repository from an image file on disk:

``` text
FileResource img = (FileResource) repositoryService.newResource(context, FileResource.class);
img.setFileType(FileResource.TYPE_IMAGE);
img.setName("logo.gif");
img.setLabel("Logo Image");
img.setDescription("Example Logo Image");
img.readData(new FileInputStream("C:\\Temp\\MyImages\\logo.gif"));
img.setParentFolder("/examples/images");
repositoryService.saveResource(context, img);
```

To retrieve a resource from the repository, you could call the following method on the `RepositoryService` instance:

``` text
// retrieve a data source resource from the repository
Resource resource = repositoryService.getResource(context,
                                                  "/datasources/mydatasource");
if (resource == null) {
  throw new RuntimeException("Resource not found at /datasources/mydatasource"); }
  if (resource instanceof JdbcReportDataSource){
    JdbcReportDataSource datasource = (JdbcReportDataSource) resource;
    System.out.println("JDBC data source URI: " + datasource.getConnectionUrl()); }
  else if (resource instanceof JndiJdbcReportDataSource) {
    JndiJdbcReportDataSource datasource = (JndiJdbcReportDataSource) resource;
    System.out.println("JNDI data source name: " + datasource.getJndiName()); }
  else {
  throw new RuntimeException
    ("Was expecting /datasources/mydatasource to be a datasource"); }
```

You can save or persist a resource in the repository by calling the following (as shown above where you created the image resource) on the `RepositoryService` instance:

``` java
public void saveResource(ExecutionContext context, Resource resource);
```

You can remove a resource from the repository by calling `repositoryService.deleteResource`:

``` text
try {
    repositoryService.deleteResource(context, "/reports/myreport");
    System.out.println("Resource /reports/myreport deleted");
} catch (Exception e) {
    System.err.println("Not able to delete resource /reports/myreport");
    e.printStackTrace();
}
```

## Content Files

Content resources are specially-created resource objects that hold binary data. The data is usually the result of using some of the BI tools available in JasperReports Server, such as the report-generating services, which produce PDF and XLS output. The output can be stored in the repository for later use, especially if the reports were generated in the background as scheduled jobs.

Creating a content resource and adding it to the repository is similar to what you've seen in the previous section, where you created an image resource:

``` text
ContentResource pdfResource = new ContentResourceImpl();
pdfResource.setFileType(ContentResource.TYPE_PDF);
pdfResource.setName("report.pdf");
pdfResource.setLabel("PDF Report");
pdfResource.setDescription("Example PDF File");
pdfResource.readData(new FileInputStream("C:\\Temp\\MyReports\\report.pdf"));
pdfResource.setParentFolder("/examples");
repositoryService.saveResource(context, pdfResource);
```

You can retrieve the binary data of a content resource from the repository using the `getContentResourceData` method of the `RepositoryService`, as follows:

``` text
FileResourceData fileResourceData =
  repositoryService.getContentResourceData(context, "/examples/report.pdf");
byte[] pdfContentBytes = fileResourceData.getData();
```

## Repository Search

You get the list of child resources within a given folder by using filter criteria. The server expects an instance of the `com.jaspersoft.jasperserver.api.metadata.view.domain.FilterCriteria` class as a parameter in the method call. The list of returned resources matches the selected filter conditions.

The only required condition for a `FilterCriteria` instance is that the returned resources’ parent folder must match a given folder. You will need to set the path to the parent folder. For example:

``` text
FilterCriteria filterCriteria = FilterCriteria.createFilter();
filterCriteria.addFilterElement(FilterCriteria.createParentFolderFilter("/examples"));
List resources = repositoryService.loadResourcesList(context, filterCriteria);
```

The `loadResourcesList` method returns a list of `ResourceLookup` objects that contain basic resource attributes like the name and label. To retrieve the full resource definition, you must use the `getResource` method. You can apply further filtering to get a refined list of resources based on a given resource type or other conditions. For example, the following retrieves all the images and JRXML files in a folder:

``` text
FilterCriteria filterCriteria = FilterCriteria.createFilter(FileResource.class);
filterCriteria.addFilterElement(FilterCriteria.createParentFolderFilter("/examples"));
FilterElementDisjunction fileTypeDisj = filterCriteria.addDisjunction();
fileTypeDisj.addFilterElement(FilterCriteria.createPropertyEqualsFilter("fileType",
  FileResource.TYPE_IMAGE);
fileTypeDisj.addFilterElement(FilterCriteria.createPropertyEqualsFilter("fileType",
  FileResource.TYPE_JRXML);
List resources = repositoryService.loadResourcesList(context, filterCriteria);
```

To develop a more detailed understanding of the filter criteria, refer to the API Javadoc.
