/***********************************/
/* Automatically created variables */
/***********************************/

/* Countries */
var namesCou = ["Slovenia", "Italy"];
var valuesCou = ["slovenia-date", "italy-date"];

/* Categories */
var namesCat = ["-2", "-1", "0", "1", "2"];
var valuesCat = ["m2", "m1", "0", "1", "2"];

/* Plan names */
var plans = ["plan0", "plan1", "plan2", "plan3", "plan4", "plan5", "plan6", "plan7", "plan8", "plan9", "planx"];

/* Not all categories are available for all countries */
var couCat = {
  "Slovenia": ["m2", "m1", "0", "1", "2"],
  "Italy": ["m2", "m1", "0"],
};

/* Not all countries are available for all categories */
var catCou = {
  "m2": ["Slovenia", "Italy"],
  "m1": ["Slovenia", "Italy"],
  "0": ["Slovenia", "Italy"],
  "1": ["Slovenia"],
  "2": ["Slovenia"],
};
