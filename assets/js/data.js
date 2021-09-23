/******************************/
/* Automatically created file */
/******************************/

/* Countries */
var namesCou = [
	"Argentina",
	"Belgium",
	"Brazil",
	"Czech Republic",
	"France",
	"Germany",
	"Greece",
	"Hungary",
	"Iran",
	"Israel",
	"Italy",
	"Malaysia",
	"Portugal",
	"Slovenia",
	"South Africa",
	"Spain",
	"Sweden",
	"Tunisia",
	"United Arab Emirates",
	"United Kingdom",
	"United States",
	"Uruguay",
];
var valuesCou = [
	"argentina",
	"belgium",
	"brazil",
	"czechrepublic",
	"france",
	"germany",
	"greece",
	"hungary",
	"iran",
	"israel",
	"italy",
	"malaysia",
	"portugal",
	"slovenia",
	"southafrica",
	"spain",
	"sweden",
	"tunisia",
	"unitedarabemirates",
	"unitedkingdom",
	"unitedstates",
	"uruguay",
];

/* Categories */
var namesCat = [
	"Infections falling steeply",
	"Infections falling",
	"Infections steady",
	"Infections rising",
	"Infections rising steeply",
];
var valuesCat = [
	"m2",
	"m1",
	"0",
	"1",
	"2",
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
	"implementedplanpredicted",
	"implementedplanreal",
];

/* Not all categories are available for all countries */
var couCat = {
	"argentina": [
		"country-argentina-20201110_category-m1",
		"country-argentina-20200925_category-0",
		"country-argentina-20210110_category-1",
		"country-argentina-20210417_category-2",
	],
	"belgium": [
		"country-belgium-20210613_category-m1",
		"country-belgium-20200401_category-1",
	],
	"brazil": [
		"country-brazil-20200718_category-0",
		"country-brazil-20201208_category-1",
	],
	"czechrepublic": [
		"country-czechrepublic-20201118_category-m2",
		"country-czechrepublic-20210127_category-m2",
		"country-czechrepublic-20210301_category-2",
	],
	"france": [
		"country-france-20201124_category-m2",
		"country-france-20210507_category-m2",
		"country-france-20210119_category-1",
		"country-france-20201026_category-2",
	],
	"germany": [
		"country-germany-20201205_category-0",
		"country-germany-20210328_category-1",
	],
	"greece": [
		"country-greece-20210505_category-m1",
	],
	"hungary": [
		"country-hungary-20201225_category-m2",
		"country-hungary-20201008_category-0",
		"country-hungary-20201110_category-2",
	],
	"iran": [
		"country-iran-20201221_category-m1",
	],
	"israel": [
		"country-israel-20201019_category-m2",
		"country-israel-20210325_category-m2",
		"country-israel-20201119_category-0",
		"country-israel-20200918_category-2",
	],
	"italy": [
		"country-italy-20201209_category-m2",
		"country-italy-20210129_category-m1",
		"country-italy-20201101_category-2",
	],
	"malaysia": [
		"country-malaysia-20210501_category-1",
	],
	"portugal": [
		"country-portugal-20210313_category-m1",
		"country-portugal-20201002_category-0",
		"country-portugal-20200404_category-1",
	],
	"slovenia": [
		"country-slovenia-20210402_category-1",
		"country-slovenia-20201025_category-2",
	],
	"southafrica": [
		"country-southafrica-20210214_category-m2",
	],
	"spain": [
		"country-spain-20210515_category-m1",
		"country-spain-20200806_category-1",
		"country-spain-20210118_category-2",
	],
	"sweden": [
		"country-sweden-20210531_category-m2",
		"country-sweden-20200712_category-m1",
		"country-sweden-20210305_category-1",
		"country-sweden-20201113_category-2",
	],
	"tunisia": [
		"country-tunisia-20210513_category-m1",
		"country-tunisia-20201208_category-0",
	],
	"unitedarabemirates": [
		"country-unitedarabemirates-20210321_category-m1",
		"country-unitedarabemirates-20200928_category-0",
	],
	"unitedkingdom": [
		"country-unitedkingdom-20210327_category-0",
	],
	"unitedstates": [
		"country-unitedstates-20210417_category-0",
	],
	"uruguay": [
		"country-uruguay-20210529_category-2",
	],
};

/* Not all countries are available for all categories */
var catCou = {
	"m2": [
		"country-czechrepublic-20201118_category-m2",
		"country-czechrepublic-20210127_category-m2",
		"country-france-20201124_category-m2",
		"country-france-20210507_category-m2",
		"country-hungary-20201225_category-m2",
		"country-israel-20201019_category-m2",
		"country-israel-20210325_category-m2",
		"country-italy-20201209_category-m2",
		"country-southafrica-20210214_category-m2",
		"country-sweden-20210531_category-m2",
	],
	"m1": [
		"country-argentina-20201110_category-m1",
		"country-belgium-20210613_category-m1",
		"country-greece-20210505_category-m1",
		"country-iran-20201221_category-m1",
		"country-italy-20210129_category-m1",
		"country-portugal-20210313_category-m1",
		"country-spain-20210515_category-m1",
		"country-sweden-20200712_category-m1",
		"country-tunisia-20210513_category-m1",
		"country-unitedarabemirates-20210321_category-m1",
	],
	"0": [
		"country-argentina-20200925_category-0",
		"country-brazil-20200718_category-0",
		"country-germany-20201205_category-0",
		"country-hungary-20201008_category-0",
		"country-israel-20201119_category-0",
		"country-portugal-20201002_category-0",
		"country-tunisia-20201208_category-0",
		"country-unitedarabemirates-20200928_category-0",
		"country-unitedkingdom-20210327_category-0",
		"country-unitedstates-20210417_category-0",
	],
	"1": [
		"country-argentina-20210110_category-1",
		"country-belgium-20200401_category-1",
		"country-brazil-20201208_category-1",
		"country-france-20210119_category-1",
		"country-germany-20210328_category-1",
		"country-malaysia-20210501_category-1",
		"country-portugal-20200404_category-1",
		"country-slovenia-20210402_category-1",
		"country-spain-20200806_category-1",
		"country-sweden-20210305_category-1",
	],
	"2": [
		"country-argentina-20210417_category-2",
		"country-czechrepublic-20210301_category-2",
		"country-france-20201026_category-2",
		"country-hungary-20201110_category-2",
		"country-israel-20200918_category-2",
		"country-italy-20201101_category-2",
		"country-slovenia-20201025_category-2",
		"country-spain-20210118_category-2",
		"country-sweden-20201113_category-2",
		"country-uruguay-20210529_category-2",
	],
};
