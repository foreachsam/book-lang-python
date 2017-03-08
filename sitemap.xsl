---
layout: sitemap-xsl
title: Sitemap
---

<div class="ui segments">

<xsl:variable name="lower" select="'abcdefghijklmnopqrstuvwxyz'" />
<xsl:variable name="upper" select="'ABCDEFGHIJKLMNOPQRSTUVWXYZ'" />
<xsl:for-each select="sitemap:urlset/sitemap:url">

	<xsl:variable name="item_url">
		<xsl:value-of select="sitemap:loc" />
	</xsl:variable>

	<div class="ui piled raised segment" >

		<div class="ui red ribbon label">
			<xsl:if test="position() mod 5 = 0">
				<xsl:attribute name="class">ui red ribbon label</xsl:attribute>
			</xsl:if>
			<xsl:if test="position() mod 5 = 1">
				<xsl:attribute name="class">ui green ribbon label</xsl:attribute>
			</xsl:if>
			<xsl:if test="position() mod 5 = 2">
				<xsl:attribute name="class">ui blue ribbon label</xsl:attribute>
			</xsl:if>
			<xsl:if test="position() mod 5 = 3">
				<xsl:attribute name="class">ui purple ribbon label</xsl:attribute>
			</xsl:if>
			<xsl:if test="position() mod 5 = 4">
				<xsl:attribute name="class">ui orange ribbon label</xsl:attribute>
			</xsl:if>
			<xsl:value-of select="concat(substring(sitemap:lastmod,0,11),concat(' ', substring(sitemap:lastmod,12,5)))" />
		</div>

		<div>
			<xsl:value-of select="concat(translate(substring(sitemap:changefreq, 1, 1),concat($lower, $upper),concat($upper, $lower)),substring(sitemap:changefreq, 2))" />
		</div>

		<div class="ui action input">
			<input type="text" value="{$item_url}" readonly="readonly" />
			<a class="ui blue icon button" href="{$item_url}" title="{$item_url}" target="_blank">
				<i class="external icon"></i>
			</a>
		</div>

	</div>
</xsl:for-each>

</div>
