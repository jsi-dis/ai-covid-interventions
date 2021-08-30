/**********************************/
/* Common variables and functions */
/**********************************/

/* Fill the columns dropdown with values */
var selectCol = document.getElementById("col");
var valuesCol = [];
var contentsCol;
for (let i = 1; i <= 10; i++) {
  valuesCol.push(i);
  contentsCol += "<option>" + i + "</option>";
}
selectCol.innerHTML = contentsCol;

/* Adds the plot to the div */
function addPlot(path, plotName) {
  let plotWidth = 100 / col.value;
  var elemDiv = document.createElement('div');
  var elemA = document.createElement('a');
  var elemImg = document.createElement("img");
  elemDiv.setAttribute("style", "display:inline-block; width:" + plotWidth + "%;");
  elemA.setAttribute("href", path + plotName);
  elemA.setAttribute("class", "nostyle");
  elemImg.setAttribute("src", path + plotName);
  elemImg.setAttribute("alt", "");
  elemA.appendChild(elemImg);
  elemDiv.appendChild(elemA);
  document.getElementById("images").appendChild(elemDiv);
}

/* Move the dropdown selection to the previous item in the list */
function getPrev(ele) {
  let select = document.getElementById(ele.id.substring(0, 3));
  let len = select.length;
  let curr_index = select.selectedIndex;
  if (curr_index > 0) {
    select.selectedIndex--;
  } else {
    select.selectedIndex = len - 1;
  }
  changePlot();
}

/* Move the dropdown selection to the next item in the list */
function getNext(ele) {
  let select = document.getElementById(ele.id.substring(0, 3));
  let len = select.length;
  let curr_index = select.selectedIndex;
  if (curr_index < len - 1) {
    select.selectedIndex++;
  } else {
    select.selectedIndex = 0;
  }
  changePlot();
}

/* Disable (or enable) the element */
function disableElements(ele, mode) {
  document.getElementById(ele + "Prev").disabled = mode;
  document.getElementById(ele).disabled = mode;
  document.getElementById(ele + "Next").disabled = mode;
  if (mode == false) {
    document.getElementById(ele + "Prev").style.cursor = "pointer";
    document.getElementById(ele).style.cursor = "pointer"
    document.getElementById(ele + "Next").style.cursor = "pointer"
  } else {
    document.getElementById(ele + "Prev").style.cursor = "default";
    document.getElementById(ele).style.cursor = "default"
    document.getElementById(ele + "Next").style.cursor = "default"
  }
}

/* Select the table cell */
function selectNode(node) {
  selectedNode = node.id;
  for (let i = 0; i < allNodes.length; i++) {
    if (selectedNode === allNodes[i]) {
      document.getElementById(allNodes[i]).className = "on";
      disableElements(allNodes[i].substring(0, 3), true);
    } else {
      document.getElementById(allNodes[i]).className = "off";
      disableElements(allNodes[i].substring(0, 3), false);
    }
  }
  changePlot();
}
