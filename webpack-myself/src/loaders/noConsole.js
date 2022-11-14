module.exports = function (content,map,meta){
    this.callback(null,content.replace(/console\.log\(.*\)/g," "),map,meta)
    return
}
