---
title: Setting Up the Jaspersoft Mobile SDK for Android
description: "Once you've installed and set up the basic configuration of SDK components and platforms, you're ready to install the Jaspersoft Mobile SDK for Android. The easiest way to install the latest version..."
---

# 1.1 Setting Up the Jaspersoft Mobile SDK for Android

Once you've installed and set up the basic configuration of SDK components and platforms, you're ready to install the Jaspersoft Mobile SDK for Android. The easiest way to install the latest version is to clone a repo and then switch to its `develop` branch.

Run the following commands

1.  git clone https://github.com/Jaspersoft/js-android-sdk.git

2.  cd js-Android-SDK/

3.  git checkout develop

4.  gradlew install

    This will install the local copy of the Jaspersoft Mobile SDK for Android as maven artifact. If you want a different version, you can checkout its tag.

5.  The main package `com.jaspersoft.android.sdk.client` provides a REST client to simplify the work with JasperReports Server REST API, a mapping of returned data to the object model, a wrapper class to work more conveniently with input controls, and an improved asynchronous tasks mechanism. To use this package, you need to add it as a compile dependency to your app.gradle file:

    <table>
    <colgroup>
    <col style="width: 100%" />
    </colgroup>
    <tbody>
    <tr>
    <td><div class="language-text highlight"><pre><code>buildscript {
        repositories {
            jcenter()
            maven { url &#39;https://raw.github.com/xujiaao/mvn-repository/master/releases&#39; }
        }
    }
    dependencies {
        compile &#39;com.jaspersoft.android.sdk:js-android-sdk-client:1.9&#39;
    }</code></pre></div></td>
    </tr>
    </tbody>
    </table>

6.  The `com.jaspersoft.android.sdk.ui` package provides a set of predefined Android adapters and layouts that help with handling data through REST and simplify UI creation. This package is no longer supported, but you can still use it and add it as a compile dependency:

    <table>
    <colgroup>
    <col style="width: 100%" />
    </colgroup>
    <tbody>
    <tr>
    <td><div class="language-text highlight"><pre><code>buildscript {
        repositories {
            jcenter()
            maven { url &#39;https://raw.github.com/xujiaao/mvn-repository/master/releases&#39; }
        }
    }
    dependencies {
        compile &#39;com.jaspersoft.android.sdk:js-android-sdk-client:1.9&#39;
        compile &#39;com.jaspersoft.android.sdk:js-android-sdk-ui:1.9&#39;
    }</code></pre></div></td>
    </tr>
    </tbody>
    </table>

7.  Optional: If you want to add Javadoc support in your IDE, the most convenient way to by using the aarLinkSources plugin. For more infomation, see <https://github.com/xujiaao/AARLinkSources>. Add the following lines to your app.gradle file:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><div class="language-text highlight"><pre><code>buildscript {
    repositories {
        jcenter()
        maven { url &#39;https://raw.github.com/xujiaao/mvn-repository/master/releases&#39; }
    }
    dependencies {
       classpath &#39;com.github.xujiaao:aarLinkSources:1.0.0&#39;
    }
}

dependencies {
    caarLinkSources &quot;com.jaspersoft.android.sdk:js-android-sdk-client:1.9:sources@jar&quot;
}</code></pre></div></td>
</tr>
</tbody>
</table>
