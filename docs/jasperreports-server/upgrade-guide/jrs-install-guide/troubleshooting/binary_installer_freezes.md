---
title: Binary Installer Freezes
description: "If you run the JasperReports Server installer on any platform and the installation fails, the following resources can help you find the source of the error."
---

# Binary Installer Freezes

If you run the JasperReports Server installer on any platform and the installation fails, the following resources can help you find the source of the error.

## Installer Log Files

If you get an error when running the JasperReports Server installer on any platform, look at the log file created by the installer. This log records the status and completion of installer operations. If a specific error occurred, you may find an explicit error message. Even without an explicit error message, the log file should help you locate the cause of the error.

You'll find the installer log for your platform in the following location:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td><p>Windows:</p></td>
<td><div class="sourceCode" id="cb1"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">js-install</span>&gt;/installation.log</span></code></pre></div></td>
</tr>
<tr>
<td><p>Linux:</p></td>
<td><div class="sourceCode" id="cb2"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">js-install</span>&gt;/installation.log</span></code></pre></div></td>
</tr>
<tr>
<td><p>Mac</p></td>
<td><div class="sourceCode" id="cb3"><pre class="sourceCode xml"><code class="sourceCode xml"><span id="cb3-1"><a href="#cb3-1" aria-hidden="true" tabindex="-1"></a>&lt;<span class="kw">js-install</span>&gt;/installation.log</span></code></pre></div></td>
</tr>
</tbody>
</table>

If you've tried multiple installs, make sure you view the most recent install log. Then you can submit the installation.log to [Jaspersoft Technical Support](https://www.jaspersoft.com/support) .

## Installer DebugTrace Mode

You can also run the installer a second time using the `--debugtrace` option. This creates a binary output file with precise details about the execution of the installer and any problems encountered. [Jaspersoft Technical Support](https://www.jaspersoft.com/support) can analyze this file.

To use the `--debugtrace` option, run the installer from the command line and specify an output filename. The precise command depends on your platform (Linux, Windows, or Mac OSX). For example, you can execute the installer with a command similar to the following:

` 10.1.0_linux_x86_64.run --debugtrace install-trace-out.bin`

When you run the installer in `--debugtrace` mode, the installer takes extra time to write the binary output file. The final size of the output file is approximately 10 mg. Contact [Jaspersoft Technical Support](https://www.jaspersoft.com/support) to hand off the binary file for analysis.
