//var nameChart = dc.rowChart("#zipcode-chart");
//var volumeChart = dc.barChart("#monthly-volume-chart");
//var yearlyBubbleChart = dc.bubbleChart("#yearly-bubble-chart");
//var rwChart = dc.geoChoroplethChart("#choropleth-map-chart");

function toTitleCase(str)
{
    return str.replace(/\w\S*/g, function(txt){return txt.charAt(0).toUpperCase() + txt.substr(1).toLowerCase();});
}

var colors = ["#a0e431","#c1d199","#5fe648","#a0a58c","#d7e747","#457138","#e4cd3c","#66e17a","#727522",
"#96e160","#dae6ba","#54b12f","#b3b985","#4a8a2a","#d5e685","#5baf5b","#b9ad58","#a1df93","#9db036","#75a067"]
queue()
	.defer(d3.csv, "populations/pop_4.csv")
	.await(ready);

function ready(error, data){
    var ndx = crossfilter(data);
    var all = ndx.groupAll();
	var headers = Object.keys(data[0])
	
	d3.select("#container").append("div").attr("class","dc-data-count")
	dc.dataCount(".dc-data-count")
	    .dimension(ndx)
	    .group(all)
	    // (optional) html, for setting different html for some records and all records.
	    // .html replaces everything in the anchor with the html given using the following function.
	    // %filter-count and %total-count are replaced with the values obtained.
	    .html({
	        some:"%filter-count selected out of <strong>%total-count</strong> records | <a href='javascript:dc.filterAll(); dc.renderAll();''>Reset All</a>",
	        all:"All  %total-count records selected."
	    })
	
		for(var h in headers){
		var className = headers[h]
			if(className !="id"){
				var newChart = makeRowChart(ndx,className,[colors[h]])
			}
	}
		var dataById = ndx.dimension(function(d){return d["id"]}).top(Infinity)
		makeDots(dataById)
	
		dc.renderAll();
};

function makeDots(dataById){	
  var tip = d3.tip()
    .attr('class', 'd3-tip')
    .offset([0, 0])

	var columns = 25
	var gridSize = 24
	var svg = d3.select("#dotsContainer").append("svg").attr("width",700).attr("height",600)
	svg.call(tip);
	svg.selectAll(".dots")
		.data(dataById)
		.enter()
		.append("circle")
		.attr("fill","#72a553")
		.attr("class",function(d){
			return "id_"+d.id
			var classString = ""
			for(var i in d){
				var key = i
				var value = d[i]
				classString+= " "+key+"_"+value
			}
			return classString
		})
		.attr("r",8)
		.attr("cx",function(d,i){
			return i%columns*gridSize+gridSize
		})
		.attr("cy",function(d,i){
			return Math.floor(i/columns)*gridSize+gridSize
		})
		.attr("cursor","pointer")
		.on('mouseover', function(d){
			var dotData = formatTipText(d)
			tip.html(dotData)
			tip.show()
			
		})
		.on('mouseout',function(d){
			tip.hide()
		})
}

function formatTipText(d){
	var str = ""
	for(var i in d){
		var key = i
		var value = d[i]
		if(value!="NA"){
			str+="<strong>"+key+"</strong>: "+value+"<br/>"
		}
	}
	return str
}
function makeTable(data){
	var table =	d3.select("#microdata").append("table")
	var row = table.append("tr")

	var header = Object.keys(data[0])	
	for(var h in header){
		console.log(h)
		row.append("th").html(header[h])
	}
	
}

function makeRowChart(ndx,column,color){
	var chartDiv = d3.select("#container").append("div").attr("class","chartDiv").attr("id",column)
	var title = chartDiv.append("div").html(column.replace("_"," ")).attr("class","chartName")
//	var graphicDiv = chartDiv.append("div").attr("id",column)
	
	var thisDimension = ndx.dimension(function(d){return d[column]})
	var thisGroup = thisDimension.group()
	
	var chart = dc.rowChart("#"+column)
	chart.width(180)
		.height(120)
	    .margins({top: 10, left: 0, right: 10, bottom: 20})
		.group(thisGroup)
		.dimension(thisDimension)
		.data(function(zipcodeGroup){return thisGroup.top(10)})
		// assign colors to each value in the x scale domain
		.ordinalColors(color)
		.label(function (d) {
		    return d.key+" : "+d.value
		})
		.labelOffsetX(5)
		.labelOffsetY(10)
		//.elasticX(true)
		.gap(1)
		.xAxis().ticks(2)
	chart.on("filtered",function(){
		var currentData = thisDimension.top(Infinity)
		var ids = {}
		d3.selectAll("circle").style("opacity",.1)
		for( var i in currentData){
			d3.select(".id_"+currentData[i].id).style("opacity",1)
		}
	})
		return chart
}