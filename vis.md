---
layout: page
permalink: /vis/
nav_order: 2
title: Intervention Visualization
---

# Intervention Visualization #
---

Show plots in 
<button id="colPrev" onclick="getPrev(this)" class="button">&minus;</button>
<select id="col" onchange="changePlot()" class="dropdown"></select>
<button id="colNext" onclick="getNext(this)" class="button">+</button> 
columns

<table BORDER="0">
<tr>
<td align="center" onclick="selectNode(this)" id="couAll" class="off"><b>Country</b></td>
<td align="center" onclick="selectNode(this)" id="catAll" class="on"><b>Category</b></td>
<td align="center" onclick="selectNode(this)" id="weiAll" class="on"><b>Weights</b></td>
<td align="center" onclick="selectNode(this)" id="graAll" class="on"><b>Granularity</b></td>
<td align="center" onclick="selectNode(this)" id="vizAll" class="on"><b>Visualization</b></td>
</tr>
<tr>
<td class="select" align="center">
<button id="couPrev" onclick="getPrev(this)" class="button"><i class="arrow left"></i></button>
<select id="cou" onchange="changePlot()" style="width:240px;"></select>
<button id="couNext" onclick="getNext(this)" class="button"><i class="arrow right"></i></button>
</td>
<td class="select" align="center">
<button id="catPrev" onclick="getPrev(this)" class="button"><i class="arrow left"></i></button>
<select id="cat" onchange="changePlot()" style="width:240px;"></select>
<button id="catNext" onclick="getNext(this)" class="button"><i class="arrow right"></i></button>
</td>
<td class="select" align="center">
<button id="weiPrev" onclick="getPrev(this)" class="button"><i class="arrow left"></i></button>
<select id="wei" onchange="changePlot()" style="width:120px;"></select>
<button id="weiNext" onclick="getNext(this)" class="button"><i class="arrow right"></i></button>
</td>
<td class="select" align="center">
<button id="graPrev" onclick="getPrev(this)" class="button"><i class="arrow left"></i></button>
<select id="gra" onchange="changePlot()" style="width:120px;"></select>
<button id="graNext" onclick="getNext(this)" class="button"><i class="arrow right"></i></button>
</td>
<td class="select" align="center">
<button id="vizPrev" onclick="getPrev(this)" class="button"><i class="arrow left"></i></button>
<select id="viz" onchange="changePlot()" style="width:240px;"></select>
<button id="vizNext" onclick="getNext(this)" class="button"><i class="arrow right"></i></button>
</td>
</tr>
</table>

<!-- <textarea id="test" rows="50" cols="100"></textarea> -->
<div id="images"></div>

<script src="{{ '/assets/js/data.js' | relative_url }}"></script>
<script src="{{ '/assets/js/common.js' | relative_url }}"></script>
<script src="{{ '/assets/js/custom.js' | relative_url }}"></script>
