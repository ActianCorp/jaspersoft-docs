---
title: Setting Up the Jaspersoft Mobile SDK for iOS
description: "These instructions are intended for those who are new to Mac or iOS development, or who have not worked extensively with 3rd-party libraries in Xcode before."
---

# 1.1 Setting Up the Jaspersoft Mobile SDK for iOS

These instructions are intended for those who are new to Mac or iOS development, or who have not worked extensively with 3rd-party libraries in Xcode before.

The recommended approach for installing the Jaspersoft Mobile SDK for iOS is through the CocoaPods package manager. CocoaPods provides flexible dependency management and very simple installation. Make sure your environments meets the minimum configuration described in [1.1, “System Requirements,” on page 1](system_requirements.md).

Run the following commands

1.  Download CocoaPods. CocoaPods is a dependency manager for Objective-C, which automates and simplifies the process of using 3rd-party libraries such as the Jaspersoft Mobile SDK in your projects. CocoaPods is distributed as a ruby gem, and is installed by running the following commands in Terminal.app:

    $ sudo gem install cocoapods

    $ pod setup

    Depending on your Ruby installation, you may not have to run as sudo to install the cocoapods gem.

2.  Project dependencies to be managed by CocoaPods are specified in a file called Podfile. Create this file in the same directory as your Xcode project (.xcodeproj) file:

    $ touch Podfile

    $ open -a Xcode Podfile

    !!! note

        Do not use TextEdit to edit the pod file because TextEdit replaces standard quotes with alternate quote characters, which causes errors in CocoaPods.

3.  Copy and paste the following lines into the new Podfile:

    <table>
    <colgroup>
    <col style="width: 100%" />
    </colgroup>
    <tbody>
    <tr>
    <td><div class="language-text highlight"><pre><code>source &#39;https://github.com/CocoaPods/Specs.git&#39;
    platform :ios, &#39;7.0&#39;
    pod &#39;JaspersoftSDK&#39;, :git =&gt; &#39;https://github.com/Jaspersoft/js-ios-sdk.git&#39;, :tag =&gt; &#39;2.0.1&#39;
    post_install do |installer_representation|
      installer_representation.project.targets.each do |target|
        if target.name == &quot;Pods-JaspersoftSDK&quot;
          target.build_configurations.each do |config|
            if config.build_settings[&#39;GCC_PREPROCESSOR_DEFINITIONS&#39;]
              config.build_settings[&#39;GCC_PREPROCESSOR_DEFINITIONS&#39;] |= [&#39;$(inherited)&#39;]
            elsif
              config.build_settings[&#39;GCC_PREPROCESSOR_DEFINITIONS&#39;] ||= [&#39;$(inherited)&#39;]
            end

        if config.name == &#39;Debug&#39;
              config.build_settings[&#39;GCC_PREPROCESSOR_DEFINITIONS&#39;] |= [&#39;__DEBUG__&#39;]
            elsif config.name == &#39;Adhoc&#39;
              config.build_settings[&#39;GCC_PREPROCESSOR_DEFINITIONS&#39;] |= [&#39;__ADHOC__&#39;]
            elsif config.name == &#39;Release&#39;
              config.build_settings[&#39;GCC_PREPROCESSOR_DEFINITIONS&#39;] |= [&#39;__RELEASE__&#39;]
            end
          end
        end
      end
    end</code></pre></div></td>
    </tr>
    </tbody>
    </table>

4.  Now you can install the dependencies in your project:

    $ pod install

5.  From now on, be sure to always open the generated Xcode workspace (.xcworkspace) instead of the project file when building your project:

    $ open &lt;YourProjectName&gt;.xcworkspace

6.  At this point, everything's in place for you to start using Jaspersoft Mobile SDK for iOS. Just #import the headers for the classes you need.

If you run into any issues with a CocoaPods based installation out of the box, the most likely cause is that your project or target contains some configuration that is overriding the settings provided via CocoaPods. CocoaPods works by adding an .xcconfig file that contains configuration aggregated from the Pods you have installed. If you augment these configuration settings within your target, you have to be sure to include the `$(inherited)` value to pick up the values provided by CocoaPods.

Please be check the following settings for overridden configuration and add `$(inherited)` if necessary:

OTHER_LDFLAGS

HEADER_SEARCH_PATHS
