/***********************************/
/* Automatically created variables */
/***********************************/

/* Countries */
var namesCou = ["Slovenia YYYY MM DD", "Italy YYYY MM DD"];
var valuesCou = ["slovenia-date", "italy-date"];

/* Categories */
var namesCat = ["-2", "-1", "0", "1", "2"];
var valuesCat = ["m2", "m1", "0", "1", "2"];

/* Plan names */
var plans = ["Plan1", "Plan2", "Plan3", "Plan4", "Plan5", "Plan6", "Plan7", "Plan8", "Plan9", "Plan10", "Implementedplan"];

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
