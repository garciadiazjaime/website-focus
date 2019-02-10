var fs = require('fs');
// const FILE_PATH = '../../../project/resources/less/sprites/empresas-sprite.less';
var FILE_PATH = '../project/resources/less/sprites/empresas-sprite.less';
var text = fs.readFileSync(FILE_PATH,'utf8')



var regex = /\.sprite(.*)\.png/gi;
var images = text.match(regex);


var regex2 = /\.sprite\("/gi;
var regex3 = /\.png/gi;

var content = '@import "sprites/empresas-sprite.less";\n\n';
images.map((item) => {
  var img = item.replace(regex2, '');
  var className = img.replace(regex3, '').toLowerCase();
  content += '.' + className + ' {\n';
  content += '\t.sprite("' + img + '", true);\n';
  content += '}\n';
});

var OUTPUT_FILE = '../project/resources/less/sprite.less';
fs.writeFile(OUTPUT_FILE, content, function(err) {
    if(err) {
        return console.log(err);
    }
    console.log("The file was saved!");
});
