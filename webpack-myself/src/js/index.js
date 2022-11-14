const arr = [[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
const test = (nums)=>{
    let res = null
    let m = new Map()
    nums.forEach((arr,index)=>{
        arr.forEach((ele)=>{
            m.set(ele,index)
        })
    })
    let arr = nums.flat()
    arr.sort((a,b)=>a-b)
    let low = 0
    let he = 0
    let count = new Map()
    console.log(arr)
    while(he <= arr.length-1){
        let index = m.get(arr[he])
        count.set(arr[he],index)
        if([...new Set([...count.values()])].length < nums.length){
            he++
        }
        else {
            while([...new Set([...count.values()])].length == nums.length ){
                count.delete(arr[low])
                if(res === null || res[1] - res [0] > arr[he] - arr[low] || (res[1] - res[0] == arr[he] - arr[low] && res[0] > arr[low]) )
                    res = [...[arr[low],arr[he]]]
                low++
            }
        }
    }
    return res
}
console.log(">>>>test",test(arr))
