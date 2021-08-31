/******************************/
/* Automatically created file */
/******************************/

/* Countries */
var namesCou = [
	"Argentina, 2020-09-25",
	"Argentina, 2021-01-10",
	"Argentina, 2021-04-17",
	"Argentina, 2020-11-10",
	"Belgium, 2020-04-01",
	"Brazil, 2020-07-18",
	"Brazil, 2020-12-08",
	"Czech Republic, 2021-03-01",
	"Czech Republic, 2020-11-18",
	"Czech Republic, 2021-01-27",
	"France, 2021-01-19",
	"France, 2020-10-26",
	"France, 2020-11-24",
	"Germany, 2020-12-05",
	"Germany, 2021-03-28",
	"Hungary, 2020-10-08",
	"Hungary, 2020-11-10",
	"Hungary, 2020-12-25",
	"Iran, 2020-12-21",
	"Israel, 2020-11-19",
	"Israel, 2020-09-18",
	"Israel, 2020-10-19",
	"Israel, 2021-03-25",
	"Italy, 2020-11-01",
	"Italy, 2021-01-29",
	"Italy, 2020-12-09",
	"Portugal, 2020-10-02",
	"Portugal, 2020-04-04",
	"Portugal, 2021-03-13",
	"Slovenia, 2021-04-02",
	"Slovenia, 2020-10-25",
	"South Africa, 2021-02-14",
	"Spain, 2020-08-06",
	"Spain, 2021-01-18",
	"Sweden, 2021-03-05",
	"Sweden, 2020-11-13",
	"Sweden, 2020-07-12",
	"Tunisia, 2020-12-08",
	"United Arab Emirates, 2020-09-28",
	"United Arab Emirates, 2021-03-21",
	"United Kingdom, 2021-03-27",
	"United States, 2021-04-17",
];
var valuesCou = [
	"argentina-20200925",
	"argentina-20210110",
	"argentina-20210417",
	"argentina-20201110",
	"belgium-20200401",
	"brazil-20200718",
	"brazil-20201208",
	"czechrepublic-20210301",
	"czechrepublic-20201118",
	"czechrepublic-20210127",
	"france-20210119",
	"france-20201026",
	"france-20201124",
	"germany-20201205",
	"germany-20210328",
	"hungary-20201008",
	"hungary-20201110",
	"hungary-20201225",
	"iran-20201221",
	"israel-20201119",
	"israel-20200918",
	"israel-20201019",
	"israel-20210325",
	"italy-20201101",
	"italy-20210129",
	"italy-20201209",
	"portugal-20201002",
	"portugal-20200404",
	"portugal-20210313",
	"slovenia-20210402",
	"slovenia-20201025",
	"southafrica-20210214",
	"spain-20200806",
	"spain-20210118",
	"sweden-20210305",
	"sweden-20201113",
	"sweden-20200712",
	"tunisia-20201208",
	"unitedarabemirates-20200928",
	"unitedarabemirates-20210321",
	"unitedkingdom-20210327",
	"unitedstates-20210417",
];

/* Categories */
var namesCat = [
	"0",
	"1",
	"2",
	"-1",
	"-2",
];
var valuesCat = [
	"0",
	"1",
	"2",
	"m1",
	"m2",
];

/* Plans */
var plans = [
	"plan1",
	"plan2",
	"plan3",
	"plan4",
	"plan5",
	"plan6",
	"plan7",
	"plan8",
	"plan9",
	"plan10",
	"implementedplan",
];

/* Not all categories are available for all countries */
var couCat = {
	"argentina-20200925": [
		"0",
	],
	"argentina-20210110": [
		"1",
	],
	"argentina-20210417": [
		"2",
	],
	"argentina-20201110": [
		"m1",
	],
	"belgium-20200401": [
		"1",
	],
	"brazil-20200718": [
		"0",
	],
	"brazil-20201208": [
		"1",
	],
	"czechrepublic-20210301": [
		"2",
	],
	"czechrepublic-20201118": [
		"m2",
	],
	"czechrepublic-20210127": [
		"m2",
	],
	"france-20210119": [
		"1",
	],
	"france-20201026": [
		"2",
	],
	"france-20201124": [
		"m2",
	],
	"germany-20201205": [
		"0",
	],
	"germany-20210328": [
		"1",
	],
	"hungary-20201008": [
		"0",
	],
	"hungary-20201110": [
		"2",
	],
	"hungary-20201225": [
		"m2",
	],
	"iran-20201221": [
		"m1",
	],
	"israel-20201119": [
		"0",
	],
	"israel-20200918": [
		"2",
	],
	"israel-20201019": [
		"m2",
	],
	"israel-20210325": [
		"m2",
	],
	"italy-20201101": [
		"2",
	],
	"italy-20210129": [
		"m1",
	],
	"italy-20201209": [
		"m2",
	],
	"portugal-20201002": [
		"0",
	],
	"portugal-20200404": [
		"1",
	],
	"portugal-20210313": [
		"m1",
	],
	"slovenia-20210402": [
		"1",
	],
	"slovenia-20201025": [
		"2",
	],
	"southafrica-20210214": [
		"m2",
	],
	"spain-20200806": [
		"1",
	],
	"spain-20210118": [
		"2",
	],
	"sweden-20210305": [
		"1",
	],
	"sweden-20201113": [
		"2",
	],
	"sweden-20200712": [
		"m1",
	],
	"tunisia-20201208": [
		"0",
	],
	"unitedarabemirates-20200928": [
		"0",
	],
	"unitedarabemirates-20210321": [
		"m1",
	],
	"unitedkingdom-20210327": [
		"0",
	],
	"unitedstates-20210417": [
		"0",
	],
};

/* Not all countries are available for all categories */
var catCou = {
	"0": [
		"argentina-20200925",
		"brazil-20200718",
		"germany-20201205",
		"hungary-20201008",
		"israel-20201119",
		"portugal-20201002",
		"tunisia-20201208",
		"unitedarabemirates-20200928",
		"unitedkingdom-20210327",
		"unitedstates-20210417",
	],
	"1": [
		"argentina-20210110",
		"belgium-20200401",
		"brazil-20201208",
		"france-20210119",
		"germany-20210328",
		"portugal-20200404",
		"slovenia-20210402",
		"spain-20200806",
		"sweden-20210305",
	],
	"2": [
		"argentina-20210417",
		"czechrepublic-20210301",
		"france-20201026",
		"hungary-20201110",
		"israel-20200918",
		"italy-20201101",
		"slovenia-20201025",
		"spain-20210118",
		"sweden-20201113",
	],
	"m1": [
		"argentina-20201110",
		"iran-20201221",
		"italy-20210129",
		"portugal-20210313",
		"sweden-20200712",
		"unitedarabemirates-20210321",
	],
	"m2": [
		"czechrepublic-20201118",
		"czechrepublic-20210127",
		"france-20201124",
		"hungary-20201225",
		"israel-20201019",
		"israel-20210325",
		"italy-20201209",
		"southafrica-20210214",
	],
};
