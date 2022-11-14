const path = require('path')

/**
 * 插件
 */
const htmlWebpackPlugin = require('html-webpack-plugin')
const {CleanWebpackPlugin} = require('clean-webpack-plugin')

module.exports = {
    //入口文件
    entry: './src/index.ts',
    //出口文件配置
    output: {
        path:path.resolve(__dirname,'dist'),
        filename: "bundle.js",
        //不使用箭头函数，ie浏览器不允许使用箭头函数，最后webpack打包的js文件的立即执行函数使用的是箭头函数，ie浏览器会报错
        environment: {
            arrowFunction: false
        }
    },
    mode: "development",
    module: {
        rules: [
            {
                //正则匹配要使用关于规则的文件
                test:/\.ts$/,
                use: [
                    /**
                     * 配置babel
                     */
                    {
                        //指定加载器
                        loader: "babel-loader",
                        options: {
                            // 设置预定义的环境
                            presets:[
                                [
                                    //指定环境插件
                                    "@babel/preset-env",
                                    {
                                        // 指定为chrome浏览器，版本为88
                                        targets:{
                                            "chrome":"88",
                                            "ie":"11"
                                        },
                                        // 指定corejs的版本
                                        "corejs":"3",
                                        // 使用corejs的方式，按需加载
                                        "useBuiltIns":"usage"
                                    }
                                ]
                            ]
                        }
                    },
                    'ts-loader'
                ],
                // 排除编译的文件
                exclude: /node-modules/
            }
        ]
    },

    resolve: {
        /**
         * 用过这个配置来告诉以ts和js结尾的文件可以作为模块使用
         * 使用export 和 import来处理不报错
         */
        extensions: ['.ts','.js']
    },
    plugins: [
        //删除上次打包的文件再打包
        new CleanWebpackPlugin(),
        //webpack服务器插件
        new htmlWebpackPlugin({
            template: "./src/index.html"
        })
    ]
}
