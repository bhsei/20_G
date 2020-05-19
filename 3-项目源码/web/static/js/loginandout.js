function loginhidden(isloginbool) {

    //
    isLogin = isloginbool;
    if(isLogin == false)//如果用户没有登录
    {
        var hidden3 = document.getElementById("navbarNavli3");//3是注册
        hidden3.style = "display:inherit;";//显示注册
        var hidden4 = document.getElementById("navbarNavli4");//4是登录
        hidden4.style = "display:inherit;";//显示登录
        var hidden5 = document.getElementById("navbarNavli5");//5是欢迎{用户名}
        hidden5.style = "display:none;";//隐藏欢迎{用户名}
    }
    else
    {
        var hidden3 = document.getElementById("navbarNavli3");//3是注册
        hidden3.style = "display:none;";//隐藏注册
        var hidden4 = document.getElementById("navbarNavli4");//4是登录
        hidden4.style = "display:none;";//隐藏登录
        var hidden5 = document.getElementById("navbarNavli5");//5是欢迎{用户名}
        hidden5.style = "display:inherit;";//显示欢迎{用户名}

        var change = document.getElementById("navbarNavli5").getElementsByTagName("a")[0]
        //change.innerText = "欢迎"+"用户名"+",退出账户";
    }
}

function jslogout(islogin) {
    /*
    *  删除Cookie，告知服务器已经退出该账号
    *
    * */
    loginhidden(islogin);
    if(islogin == true)
    {
        //已经登录，什么都不用做
    }
    else{
        //已经退出账号，需要告知用户已经退出
        alert("您已经退出账户");
    }
}

function hasCookie(){


    return true;
}


function hasCookie(){
    if (navigator.cookieEnabled==false)
    {
        alert("请设置浏览器为 开启 Cookie 状态");
    }

}


//获得coolie 的值
function Cookie(name){
  var cookieArray = document.cookie.split("; ");//得到分割的cookie名值对
  var cookie = new Object();
  for(var i=0; i<cookieArray.length; i++){
    var arr = cookieArray[i].split("=");//将名和值分开
    if(arr[0]==name)
        return unescape(arr[1]);//如果是指定的cookie，则返回它的值
  }
  return "";
}

//删除cookie
function delCookie(name){
  document.cookie = name+"=;expires="+(new Date(0)).toGMTString();
}

//获取指定名称的cookie的值
function getCookie(objName){
  var arrStr=document.cookie.split("; ");
  for(var i = 0;i < arrStr.length;i ++){
    var temp=arrStr[i].split("=");
    if(temp[0]==objName) return unescape(temp[1]);
  }
}

loginhidden(true);//默认为已经登录，应根据Cookie来进行
//loginhidden(hasCookie());


