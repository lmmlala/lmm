const path = require("path");
const EsLintPlugin = require('eslint-webpack-plugin')
const HtmlWebpackPlugin = require('html-webpack-plugin');
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const CssMinimizerPlugin = require("css-minimizer-webpack-plugin");
// const TerserWebpackPlugin = require("terser-webpack-plugin")

//获取cpu的核数
// const os = require("os");
// const threads = os.cpus().length;

module.exports = {
    entry: './main.js',
    output: {
        filename: "main.js",
        path:path.resolve(__dirname,"dist"),
        assetModuleFilename: "src/images/[hash][ext][query]",
        clean: true //保证每次打包删除上次打包的内容
    },
    module: {
        rules: [
            {
                test:/.css$/,
                use:[MiniCssExtractPlugin.loader,'css-loader']
            },
            {
                test:/.less$/,
                use:[MiniCssExtractPlugin.loader,'css-loader','less-loader']
            },
            {
                test:/\.(png|jpe?g)/,
                type: "asset",
                parser:{
                    dataUrlCondition:{
                        maxSize:4*1024 // 4kb
                    }
                }
            },
            {
                test:/.txt$/,
                type:"asset/source"
            },
            {
                test: /\.m?js$/,
                exclude: /(node_modules|bower_components)/,
                use:[
                    //注意要在babel-loader之前
                    // {
                    //     loader: "thread-loader",
                    //     options: {
                    //         works:threads,
                    //     }
                    // },
                    {
                        loader: 'babel-loader',
                        options: {
                            presets: ['@babel/preset-env'],
                            plugins: ["@babel/plugin-transform-runtime"]
                        }
                    }
                ]
            }
        ]
    },
    mode:"development",
    devtool: "cheap-module-source-map",
    plugins: [
        new EsLintPlugin({
            context:path.resolve(__dirname,"src"),
            // threads // eslint开启多进程
        }),
        new HtmlWebpackPlugin ({
            // 模板，以public/index.html文件创建新的html文件
            // 新的html文件自动引入打包输出的资源
            template: path.resolve(__dirname,"public/index.html")
        }),
        new MiniCssExtractPlugin({
            // 最后输出的文件路径
            filename:"static/css/main.css"
        }),
        new CssMinimizerPlugin()

    ],
    devServer: {
        host:"localhost",
        port:"3030",
        // 是否自动打开浏览器
        open:true,
        hot:true, //开启热模块打包,仅适用开发环境，在生产环境不需要了
    },
    // 压缩开启多进程
    // optimization: {
    //     minimizer: [
    //         new CssMinimizerPlugin(),
    //         new TerserWebpackPlugin({
    //             parallel:threads
    //         })
    //     ]
    // }
}
