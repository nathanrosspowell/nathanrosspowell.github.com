/*! nathanrosspowell.github.com - v0.0.0 - 2014-06-26 */var swfobject=function(){function a(){if(!R){try{var a=K.getElementsByTagName("body")[0].appendChild(q("span"));a.parentNode.removeChild(a)}catch(b){return}R=!0;for(var c=N.length,d=0;c>d;d++)N[d]()}}function b(a){R?a():N[N.length]=a}function c(a){if(typeof J.addEventListener!=C)J.addEventListener("load",a,!1);else if(typeof K.addEventListener!=C)K.addEventListener("load",a,!1);else if(typeof J.attachEvent!=C)r(J,"onload",a);else if("function"==typeof J.onload){var b=J.onload;J.onload=function(){b(),a()}}else J.onload=a}function d(){M?e():f()}function e(){var a=K.getElementsByTagName("body")[0],b=q(D);b.setAttribute("type",G);var c=a.appendChild(b);if(c){var d=0;!function(){if(typeof c.GetVariable!=C){var e=c.GetVariable("$version");e&&(e=e.split(" ")[1].split(","),U.pv=[parseInt(e[0],10),parseInt(e[1],10),parseInt(e[2],10)])}else if(10>d)return d++,void setTimeout(arguments.callee,10);a.removeChild(b),c=null,f()}()}else f()}function f(){var a=O.length;if(a>0)for(var b=0;a>b;b++){var c=O[b].id,d=O[b].callbackFn,e={success:!1,id:c};if(U.pv[0]>0){var f=p(c);if(f)if(!s(O[b].swfVersion)||U.wk&&U.wk<312)if(O[b].expressInstall&&h()){var k={};k.data=O[b].expressInstall,k.width=f.getAttribute("width")||"0",k.height=f.getAttribute("height")||"0",f.getAttribute("class")&&(k.styleclass=f.getAttribute("class")),f.getAttribute("align")&&(k.align=f.getAttribute("align"));for(var l={},m=f.getElementsByTagName("param"),n=m.length,o=0;n>o;o++)"movie"!=m[o].getAttribute("name").toLowerCase()&&(l[m[o].getAttribute("name")]=m[o].getAttribute("value"));i(k,l,c,d)}else j(f),d&&d(e);else u(c,!0),d&&(e.success=!0,e.ref=g(c),d(e))}else if(u(c,!0),d){var q=g(c);q&&typeof q.SetVariable!=C&&(e.success=!0,e.ref=q),d(e)}}}function g(a){var b=null,c=p(a);if(c&&"OBJECT"==c.nodeName)if(typeof c.SetVariable!=C)b=c;else{var d=c.getElementsByTagName(D)[0];d&&(b=d)}return b}function h(){return!S&&s("6.0.65")&&(U.win||U.mac)&&!(U.wk&&U.wk<312)}function i(a,b,c,d){S=!0,y=d||null,z={success:!1,id:c};var e=p(c);if(e){"OBJECT"==e.nodeName?(w=k(e),x=null):(w=e,x=c),a.id=H,(typeof a.width==C||!/%$/.test(a.width)&&parseInt(a.width,10)<310)&&(a.width="310"),(typeof a.height==C||!/%$/.test(a.height)&&parseInt(a.height,10)<137)&&(a.height="137"),K.title=K.title.slice(0,47)+" - Flash Player Installation";var f=U.ie&&U.win?"ActiveX":"PlugIn",g="MMredirectURL="+J.location.toString().replace(/&/g,"%26")+"&MMplayerType="+f+"&MMdoctitle="+K.title;if(typeof b.flashvars!=C?b.flashvars+="&"+g:b.flashvars=g,U.ie&&U.win&&4!=e.readyState){var h=q("div");c+="SWFObjectNew",h.setAttribute("id",c),e.parentNode.insertBefore(h,e),e.style.display="none",function(){4==e.readyState?e.parentNode.removeChild(e):setTimeout(arguments.callee,10)}()}l(a,b,c)}}function j(a){if(U.ie&&U.win&&4!=a.readyState){var b=q("div");a.parentNode.insertBefore(b,a),b.parentNode.replaceChild(k(a),b),a.style.display="none",function(){4==a.readyState?a.parentNode.removeChild(a):setTimeout(arguments.callee,10)}()}else a.parentNode.replaceChild(k(a),a)}function k(a){var b=q("div");if(U.win&&U.ie)b.innerHTML=a.innerHTML;else{var c=a.getElementsByTagName(D)[0];if(c){var d=c.childNodes;if(d)for(var e=d.length,f=0;e>f;f++)1==d[f].nodeType&&"PARAM"==d[f].nodeName||8==d[f].nodeType||b.appendChild(d[f].cloneNode(!0))}}return b}function l(a,b,c){var d,e=p(c);if(U.wk&&U.wk<312)return d;if(e)if(typeof a.id==C&&(a.id=c),U.ie&&U.win){var f="";for(var g in a)a[g]!=Object.prototype[g]&&("data"==g.toLowerCase()?b.movie=a[g]:"styleclass"==g.toLowerCase()?f+=' class="'+a[g]+'"':"classid"!=g.toLowerCase()&&(f+=" "+g+'="'+a[g]+'"'));var h="";for(var i in b)b[i]!=Object.prototype[i]&&(h+='<param name="'+i+'" value="'+b[i]+'" />');e.outerHTML='<object classid="clsid:D27CDB6E-AE6D-11cf-96B8-444553540000"'+f+">"+h+"</object>",P[P.length]=a.id,d=p(a.id)}else{var j=q(D);j.setAttribute("type",G);for(var k in a)a[k]!=Object.prototype[k]&&("styleclass"==k.toLowerCase()?j.setAttribute("class",a[k]):"classid"!=k.toLowerCase()&&j.setAttribute(k,a[k]));for(var l in b)b[l]!=Object.prototype[l]&&"movie"!=l.toLowerCase()&&m(j,l,b[l]);e.parentNode.replaceChild(j,e),d=j}return d}function m(a,b,c){var d=q("param");d.setAttribute("name",b),d.setAttribute("value",c),a.appendChild(d)}function n(a){var b=p(a);b&&"OBJECT"==b.nodeName&&(U.ie&&U.win?(b.style.display="none",function(){4==b.readyState?o(a):setTimeout(arguments.callee,10)}()):b.parentNode.removeChild(b))}function o(a){var b=p(a);if(b){for(var c in b)"function"==typeof b[c]&&(b[c]=null);b.parentNode.removeChild(b)}}function p(a){var b=null;try{b=K.getElementById(a)}catch(c){}return b}function q(a){return K.createElement(a)}function r(a,b,c){a.attachEvent(b,c),Q[Q.length]=[a,b,c]}function s(a){var b=U.pv,c=a.split(".");return c[0]=parseInt(c[0],10),c[1]=parseInt(c[1],10)||0,c[2]=parseInt(c[2],10)||0,b[0]>c[0]||b[0]==c[0]&&b[1]>c[1]||b[0]==c[0]&&b[1]==c[1]&&b[2]>=c[2]?!0:!1}function t(a,b,c,d){if(!U.ie||!U.mac){var e=K.getElementsByTagName("head")[0];if(e){var f=c&&"string"==typeof c?c:"screen";if(d&&(A=null,B=null),!A||B!=f){var g=q("style");g.setAttribute("type","text/css"),g.setAttribute("media",f),A=e.appendChild(g),U.ie&&U.win&&typeof K.styleSheets!=C&&K.styleSheets.length>0&&(A=K.styleSheets[K.styleSheets.length-1]),B=f}U.ie&&U.win?A&&typeof A.addRule==D&&A.addRule(a,b):A&&typeof K.createTextNode!=C&&A.appendChild(K.createTextNode(a+" {"+b+"}"))}}}function u(a,b){if(T){var c=b?"visible":"hidden";R&&p(a)?p(a).style.visibility=c:t("#"+a,"visibility:"+c)}}function v(a){var b=/[\\\"<>\.;]/,c=null!=b.exec(a);return c&&typeof encodeURIComponent!=C?encodeURIComponent(a):a}{var w,x,y,z,A,B,C="undefined",D="object",E="Shockwave Flash",F="ShockwaveFlash.ShockwaveFlash",G="application/x-shockwave-flash",H="SWFObjectExprInst",I="onreadystatechange",J=window,K=document,L=navigator,M=!1,N=[d],O=[],P=[],Q=[],R=!1,S=!1,T=!0,U=function(){var a=typeof K.getElementById!=C&&typeof K.getElementsByTagName!=C&&typeof K.createElement!=C,b=L.userAgent.toLowerCase(),c=L.platform.toLowerCase(),d=/win/.test(c?c:b),e=/mac/.test(c?c:b),f=/webkit/.test(b)?parseFloat(b.replace(/^.*webkit\/(\d+(\.\d+)?).*$/,"$1")):!1,g=!1,h=[0,0,0],i=null;if(typeof L.plugins!=C&&typeof L.plugins[E]==D)i=L.plugins[E].description,!i||typeof L.mimeTypes!=C&&L.mimeTypes[G]&&!L.mimeTypes[G].enabledPlugin||(M=!0,g=!1,i=i.replace(/^.*\s+(\S+\s+\S+$)/,"$1"),h[0]=parseInt(i.replace(/^(.*)\..*$/,"$1"),10),h[1]=parseInt(i.replace(/^.*\.(.*)\s.*$/,"$1"),10),h[2]=/[a-zA-Z]/.test(i)?parseInt(i.replace(/^.*[a-zA-Z]+(.*)$/,"$1"),10):0);else if(typeof J.ActiveXObject!=C)try{var j=new ActiveXObject(F);j&&(i=j.GetVariable("$version"),i&&(g=!0,i=i.split(" ")[1].split(","),h=[parseInt(i[0],10),parseInt(i[1],10),parseInt(i[2],10)]))}catch(k){}return{w3:a,pv:h,wk:f,ie:g,win:d,mac:e}}();!function(){U.w3&&((typeof K.readyState!=C&&"complete"==K.readyState||typeof K.readyState==C&&(K.getElementsByTagName("body")[0]||K.body))&&a(),R||(typeof K.addEventListener!=C&&K.addEventListener("DOMContentLoaded",a,!1),U.ie&&U.win&&(K.attachEvent(I,function(){"complete"==K.readyState&&(K.detachEvent(I,arguments.callee),a())}),J==top&&!function(){if(!R){try{K.documentElement.doScroll("left")}catch(b){return void setTimeout(arguments.callee,0)}a()}}()),U.wk&&!function(){return R?void 0:/loaded|complete/.test(K.readyState)?void a():void setTimeout(arguments.callee,0)}(),c(a)))}(),function(){U.ie&&U.win&&window.attachEvent("onunload",function(){for(var a=Q.length,b=0;a>b;b++)Q[b][0].detachEvent(Q[b][1],Q[b][2]);for(var c=P.length,d=0;c>d;d++)n(P[d]);for(var e in U)U[e]=null;U=null;for(var f in swfobject)swfobject[f]=null;swfobject=null})}()}return{registerObject:function(a,b,c,d){if(U.w3&&a&&b){var e={};e.id=a,e.swfVersion=b,e.expressInstall=c,e.callbackFn=d,O[O.length]=e,u(a,!1)}else d&&d({success:!1,id:a})},getObjectById:function(a){return U.w3?g(a):void 0},embedSWF:function(a,c,d,e,f,g,j,k,m,n){var o={success:!1,id:c};U.w3&&!(U.wk&&U.wk<312)&&a&&c&&d&&e&&f?(u(c,!1),b(function(){d+="",e+="";var b={};if(m&&typeof m===D)for(var p in m)b[p]=m[p];b.data=a,b.width=d,b.height=e;var q={};if(k&&typeof k===D)for(var r in k)q[r]=k[r];if(j&&typeof j===D)for(var t in j)typeof q.flashvars!=C?q.flashvars+="&"+t+"="+j[t]:q.flashvars=t+"="+j[t];if(s(f)){var v=l(b,q,c);b.id==c&&u(c,!0),o.success=!0,o.ref=v}else{if(g&&h())return b.data=g,void i(b,q,c,n);u(c,!0)}n&&n(o)})):n&&n(o)},switchOffAutoHideShow:function(){T=!1},ua:U,getFlashPlayerVersion:function(){return{major:U.pv[0],minor:U.pv[1],release:U.pv[2]}},hasFlashPlayerVersion:s,createSWF:function(a,b,c){return U.w3?l(a,b,c):void 0},showExpressInstall:function(a,b,c,d){U.w3&&h()&&i(a,b,c,d)},removeSWF:function(a){U.w3&&n(a)},createCSS:function(a,b,c,d){U.w3&&t(a,b,c,d)},addDomLoadEvent:b,addLoadEvent:c,getQueryParamValue:function(a){var b=K.location.search||K.location.hash;if(b){if(/\?/.test(b)&&(b=b.split("?")[1]),null==a)return v(b);for(var c=b.split("&"),d=0;d<c.length;d++)if(c[d].substring(0,c[d].indexOf("="))==a)return v(c[d].substring(c[d].indexOf("=")+1))}return""},expressInstallCallback:function(){if(S){var a=p(H);a&&w&&(a.parentNode.replaceChild(w,a),x&&(u(x,!0),U.ie&&U.win&&(w.style.display="block")),y&&y(z)),S=!1}}}}();