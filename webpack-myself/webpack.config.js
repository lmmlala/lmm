const path = require('path')
module.exports = {
    entry: path.resolve(__dirname,'main.js'),
    output: {
        filename: "dist/index.js",
        clean: true,
    },
    module: {
        rules: [
            {
                test: /\.js$/,
                use:['./src/loaders/noConsole.js',
                    {
                        loader: "./src/loaders/banner-loader.js",
                        options: {
                            name:"lmm"
                        }
                    }
                ]
            }
        ]
    },
    mode:"development",
}
