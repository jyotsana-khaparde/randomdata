function sleep(time) {
   return new Promise(resolve => setTimeout(resolve, time));
}

const load = async () => {
    for (let i = 1; i < 10000 ; i++) {
        await sleep(900000) //wait for 15 min. (900000)
        console.log("tested load of workflow( "+ i +" )times");;
    }
}

load()