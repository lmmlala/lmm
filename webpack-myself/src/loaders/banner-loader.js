const schema = require("./schema.json")

module.exports = function (content){
    const options = this.getOptions(schema)
    const prefix = `
        /**
        *   name:${options.name}
        **/
    `
    return prefix + content
}
