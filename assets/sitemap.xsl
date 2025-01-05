<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">
        <html>
            <head>
                <title>XML Sitemap</title>
                <style>
                    body {
                        font-family: Arial, sans-serif;
                        margin: 20px;
                    }
                    table {
                        width: 100%;
                        border-collapse: collapse;
                    }
                    th, td {
                        padding: 8px;
                        border: 1px solid #ddd;
                        text-align: left;
                    }
                    th {
                        background-color: #f2f2f2;
                    }
                </style>
            </head>
            <body>
                <h1>XML Sitemap</h1>
                <table>
                    <tr>
                        <th>URL</th>
                        <th>Last Modified</th>
                    </tr>
                    <xsl:for-each select="sitemapindex/sitemap">
                        <tr>
                            <td><xsl:value-of select="loc" /></td>
                            <td><xsl:value-of select="lastmod" /></td>
                        </tr>
                    </xsl:for-each>
                </table>
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>
