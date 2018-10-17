//queue()
//  .defer(d3.csv,"centroids.csv")
//  .await(dataDidLoad);
//
//function dataDidLoad(error,centroidsFile,keysFile,dataFile) { 
//
//}

var population = 100
var w = 600

d3.select("#chart")
		.append("svg").attr("width",w).attr("height",w)

drawDots(population,"#648ace",0,"b")
drawDots(population,"#6ca659",w/2,"w")

function drawDots(population,color,margin,className){
	var ids = new Array(population)
	
	var svg = d3.select("#chart svg")
	var col = 20
	var cellSize = 12
	var r = 5
	
	svg.selectAll("."+className)
		.data(ids)
		.enter()
		.append("circle")
		.attr("class",function(d,i){
			return className+"_"+i
		})
		.attr("cx",function(d,i){
			return i%col*cellSize+cellSize+margin
		})
		.attr("cy",function(d,i){
			return Math.floor(i/col)*cellSize+cellSize
		})
		.attr("r",r)
		.attr("fill",color)
		.style("opacity",0)
		.transition()
		.duration(1000)
		.delay(function(d,i){return i*20})
		.style("opacity",1)
}

var education = [146,113,59]

function gotoBin(data){
	
	
}