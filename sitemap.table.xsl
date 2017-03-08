---
layout: sitemap-xsl
title: Sitemap
---

<table class="ui selectable collapsing striped table">
	<thead>
		<th>
			<div>連結</div>
		</th>
		<th align="right">
			<div>最近更新</div>
		</th>
		<th align="right">
			<div>更新頻率</div>
		</th>
	</thead>
	<tbody>
		<xsl:variable name="lower" select="'abcdefghijklmnopqrstuvwxyz'" />
		<xsl:variable name="upper" select="'ABCDEFGHIJKLMNOPQRSTUVWXYZ'" />
		<xsl:for-each select="sitemap:urlset/sitemap:url">
		<tr>
			<xsl:if test="position() mod 2 != 0">
				<xsl:attribute name="class">row-odd</xsl:attribute>
			</xsl:if>
			<xsl:if test="position() mod 2 != 1">
				<xsl:attribute name="class">row-even</xsl:attribute>
			</xsl:if>
			<xsl:variable name="item_url">
				<xsl:value-of select="sitemap:loc" />
			</xsl:variable>
			<td align="center">
				<div class="ui action input">
					<input type="text" value="{$item_url}" readonly="readonly" />
					<a class="ui blue icon button" href="{$item_url}" title="{$item_url}" target="_blank">
						<i class="content icon"></i>
					</a>
				</div>
			</td>
			<td align="right">
				<div>
					<xsl:value-of select="concat(substring(sitemap:lastmod,0,11),concat(' ', substring(sitemap:lastmod,12,5)))" />
				</div>
			</td>
			<td align="right">
				<div>
					<xsl:value-of select="concat(translate(substring(sitemap:changefreq, 1, 1),concat($lower, $upper),concat($upper, $lower)),substring(sitemap:changefreq, 2))" />
				</div>
			</td>
		</tr>
		</xsl:for-each>
	</tbody>
</table>
