/**************************************************************/
/* Functions for the Visualizations of multiple features page */
/**************************************************************/

selectCol.options[2].selected = true;

/* Url to the plots */
plotPath = "../assets/img/plots/";

/* Fill the country dropdown with values */
var selectCou = document.getElementById("cou");
/* valuesCou is read from data.js */
var contentsCou;
for (let i = 0; i < valuesCou.length; i++) {
  contentsCou += "<option value=\"" + valuesCou[i] + "\">" + namesCou[i] + "</option>";
}
selectCou.innerHTML = contentsCou;

/* Fill the category dropdown with values */
var selectCat = document.getElementById("cat");
/* valuesCat and namesCat are read from data.js */
var contentsCat;
for (let i = 0; i < valuesCat.length; i++) {
  contentsCat += "<option value=\"" + valuesCat[i] + "\">" + namesCat[i] + "</option>";
}
selectCat.innerHTML = contentsCat;

/* Fill the weights dropdown with values */
var selectWei = document.getElementById("wei");
var namesWei = ["Social", "GDP", "Combined"];
var valuesWei = ["social", "gdp", "combined"];
var contentsWei;
for (let i = 0; i < valuesWei.length; i++) {
  contentsWei += "<option value=\"" + valuesWei[i] + "\">" + namesWei[i] + "</option>";
}
selectWei.innerHTML = contentsWei;

/* Fill the visualization dropdown with values */
var selectViz = document.getElementById("viz");
var valuesViz = ["various", "plans"];
var namesViz = ["Infections and stringency", "Intervention plans"];
var plots = ["infections", "stringency", "objectives"];
var contentsViz;
for (let i = 0; i < valuesViz.length; i++) {
  contentsViz += "<option value=\"" + valuesViz[i] + "\">" + namesViz[i] + "</option>";
}
selectViz.innerHTML = contentsViz;

/* By default, countries are chosen */
var allNodes = ["couAll", "catAll", "weiAll", "vizAll"];
var selectedNode = "couAll";
selectNode(document.getElementById(selectedNode));

/* Show the plots wrt the chosen country, category, weights and visualization.
Exactly one of these categories contains all possible values, the rest only the chosen one. */
function changePlot() {
	var plotName;
	var chosenWei = [wei.value];
	var chosenViz = [viz.value];
	var textName;
	document.getElementById("images").innerHTML = "";
	// document.getElementById("test").value = "";
	var chosenCC = [];
	if (selectedNode === "couAll") {
		chosenCC = catCou[cat.value];
	} else if (selectedNode === "catAll") {
		chosenCC = couCat[cou.value];
	} else if (selectedNode === "weiAll") {
		chosenWei = [...valuesWei];
		chosenCC = catCou[cat.value].filter(function(n) {
            return couCat[cou.value].indexOf(n) !== -1;
        })
	} else if (selectedNode === "vizAll") {
		chosenViz = [...valuesViz];
		chosenCC = catCou[cat.value].filter(function(n) {
            return couCat[cou.value].indexOf(n) !== -1;
        })
	}
	for (var iCC = 0; iCC < chosenCC.length; iCC++) {
        for (var iWei = 0; iWei < chosenWei.length; iWei++) {
            for (var iViz = 0; iViz < chosenViz.length; iViz++) {
                if (chosenViz[iViz] === 'various')  {
                    for (let i = 0; i < plots.length; i++) {
                        plotName = chosenCC[iCC] + "_" + "weights-" + chosenWei[iWei] + "_" + "viz-" + plots[i] + ".png";
                        addPlot(plotPath, plotName);
                        // document.getElementById("test").value += plotName + "\n";
                    }
                }
                else {
                    for (let i = 0; i < plans.length; i++) {
                        plotName = chosenCC[iCC] + "_" + "weights-" + chosenWei[iWei] + "_" + "viz-" + plans[i] + ".png";
                        addPlot(plotPath, plotName);
                        // document.getElementById("test").value += plotName + "\n";
                    }
                }
            }
        }
	}
}