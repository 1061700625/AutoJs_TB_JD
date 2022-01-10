auto()

console.show()

function debug(msg) {
    log(msg);
}

function waitForNoElement(element, timeout) {
    var cnt = 0
    while(cnt < timeout) {
        if(!element.exists()) {
            debug('元素已消失')
            return true
        }
        sleep(1000);
        cnt += 1000;
        debug('等待1s...');
    }
    return false
}

function waitForElement(element, timeout) {
    var cnt = 0
    while(cnt < timeout) {
        if(element.exists()) {
            debug('找到元素')
            return true
        }
        sleep(1000);
        cnt += 1000;
        debug('等待1s...');
    }
    return false
}

// 进入活动页面
function enterActivity() {
    app.launch('com.jingdong.app.mall');
    sleep(2000);
    var ns = className("android.widget.ImageView").desc("浮层活动");
    if(ns.exists()){
        ns.click();
        ns = ns.findOne();
        click(ns.bounds().centerX(), ns.bounds().centerY());
        sleep(200);
        click(ns.bounds().centerX(), ns.bounds().centerY());
        debug('进入活动');
    }
    if(!className("android.view.View").textContains("我的爆竹").exists()) {
        waitForElement(className("android.view.View").textContains("我的爆竹"), 10000);
    }    
    debug('进入成功')
}

// 打开任务列表
function openTaskList() {
    debug('打开任务列表')
    var taskBtn = className("android.view.View").depth(14).indexInParent(19);
    taskBtn.findOne().click();
    sleep(1000);
}

// 获取任务列表
function taskList() {
    var list = className("android.view.View").depth(19).indexInParent(2).find();
    if(list.length == 0) {
        alert('请手动打开任务列表~');
    }
    var res = []
    list.forEach((child) => {
        if(child.text() != '') {
            res.push(child.parent());
        }
    });
    return res
}

// 加入会员任务
function tobeVip(item) {
    var btn = item.child(3);
    btn.click();
    // TODO
}

// 浏览商品任务
function doBrowse(item) {
    var btn = item.child(3);
    btn.click();
    sleep(2000);
    waitForNoElement(className("android.view.View").text('下拉有惊喜'), 10000);
    sleep(2000);

    if(className("android.view.View").text('即将离开京东').exists()) {
        className("android.view.View").text('取消').findOne().click();
        back();
        return;
    }
    if(className("android.widget.TextView").text('互动种草城').exists()) {
        var shopLists = className("android.view.View").text('去完成去完成').find();
        for(var i=0; i < 3; i++) {
            var shop = shopLists[i];
            click(shop.bounds().centerX(), shop.bounds().centerY());
            sleep(1000);
            back()
            sleep(2000);
        }
        return;
    }

    if(waitForElement(className("android.view.View").textContains('得8000爆竹'), 10000)) {
        debug('等待10s')
        waitForElement(className("android.widget.TextView").text('获得8000爆竹'), 15000)
    }
    back();
}


// 加购商品任务
function addGoods(item) {
    var btn = item.child(3);
    btn.click();
    sleep(1000);
    waitForElement(className("android.view.View").textContains('当前页浏览加购'), 1000);
    var addBtnList = className("android.view.View").depth(15).indexInParent(4).find();
    debug(addBtnList.length)
    for(var i=0; i < 4; i++) {
        var good = addBtnList[i];
        good.click();
        sleep(1000);
        back();
        sleep(1000);
        debug('成功加购1个商品')
    };

    back();
}


// 执行一系列任务入口
function doTasks(tasks) {
    var taskDoneCnt = 0
    tasks.forEach((task) => {
        var image = task.child(0);
        var title = task.child(1);
        var desc = task.child(2);
        var btn = task.child(3);
        if(title == null) {
            return true;
        }
        if(title.text().indexOf('邀请好友') != -1) {
            taskDoneCnt += 1;
            return true;
        }

        var doneCnt = parseInt(title.text().slice(-4,-3))
        var totalCnt = parseInt(title.text().slice(-2,-1))
        if(doneCnt == totalCnt) {
            debug('['+title.text()+'] 任务已完成，跳过')
            taskDoneCnt += 1;
            return true;
        }

        if(title.text().indexOf('去加购') != -1) {
            debug('['+title.text()+'] 开始加购任务')
            addGoods(task);
            debug('加购任务完成一次')
            return true;
        }

        if(desc.text().indexOf('成功入会') != -1) {
            debug('['+title.text()+'] 跳过入会任务')
            taskDoneCnt += 1;
            return true;
        }
        

        if(desc.text().indexOf('浏览') != -1) {
            debug('['+title.text()+'] 开始浏览任务');
            doBrowse(task);
            debug('浏览任务完成一次')
            return true;
        }
    });
    return taskDoneCnt;
}






enterActivity()
openTaskList()
var taskDoneCnt = 0;
while(taskDoneCnt < 5) {
    var tasks = taskList()
    taskDoneCnt = doTasks(tasks)
    sleep(1000)
}
debug('')
debug('全部完成，感谢使用~ ♪(･ω･)ﾉ')


