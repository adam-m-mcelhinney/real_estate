/* Copyright 2008-2013 Adometry, Inc. */
try{var DMTRY=DMTRY||{};DMTRY.CHANNEL=DMTRY.CHANNEL||{};(function(){var b="undefined",c="v",e="c";var a=DMTRY.CHANNEL;a.directory=a.directory||[];a.session=a.session||d(999999);a.sendError=function(g){var h="log.dmtry.com",f="http://"+h+"/1.ver?at=e&d=ChannelError&msg="+encodeURIComponent(g);a.sendRequest(f)};a.sendRequest=function(g){var h=2048,f=new Image;f.border=0;f.vspace=0;f.hspace=0;f.height=1;f.width=1;if(f){if(g!=null&&g!=""){g=g.substring(0,h);if(g.length>0){f.src=g}}}else{throw new Error("No image created for log event")}return g};function d(f){var g=Math.random()*(f)+1;return Math.floor(g)}(function(g){var l={};try{var h=function(B){var A=this;A.qsPropertyKeys=B||[];A.propertyMap={}};l.scriptProps=null;l.isMaster=(g===0)?true:false;l.config={brand:"DMTRY",fPattern:/channel\.js/,host:"log.dmtry.com",ver:"chl-1.3.4",PATHORDER:["rand","bid","gid","pid","cid","sid","aid","srcid","advid"],TRANSLATE:{},SEND_ONCE:["csync"]};l.actions={refer:new h(["at","d","jsv","csync","if","rev","chl_pass","chl","unk","pg"]),link:new h(["at","d","jsv","csync","if","rev","chl_pass","chl","unk","pg"])};l.sendError=function(B){var A=t(l.config,l.scriptProps)+z(l.config,l.loggingProps)+"?at=e&d=ChannelInstError&msg="+encodeURIComponent(B);a.sendRequest(A)};var v=function(){var E={winObj:window,levelsUp:0},D=20,G=false,F=false,C;for(var B=window,A=0;;B=B.parent,A++){if(A==D){A=-1;break}try{if(B.document){E.winObj=B;E.levelsUp=A}else{F=true}}catch(H){F=true}if(B==B.parent){break}else{G=true}}C=A;return{bestWinObj:E.winObj,isTop:(C==E.levelsUp),inFrame:G,nonFriendlyPresent:F}};var o=function(A){if(A==null){throw new Error("invalid config")}var G={elem:null,protocol:"http",hash:null},C=A.brand||"tagproc",D=document.getElementsByTagName("script"),F,B,E;for(B=0;B<D.length;B++){G.elem=D[B];F=G.elem.src;if(F.search(A.fPattern)>=0&&G.elem[C]===undefined){G.elem[C]=true;E=F.indexOf(":");if(E>0){G.protocol=F.substring(0,E)}E=(F.indexOf("js#")>0)?F.indexOf("js#"):F.indexOf("js?");if(E>0){G.hash=F.substring(E+3,F.length)}}}return G};var w=function(A,C){if(A==null){throw new Error("invalid config")}var B=v();u(A,C,B);if(l.isMaster===true){p(A,C,B)}};var u=function(C,F,D){var A="refer",G=F.hash,B={};try{B=l.actions[A].propertyMap}catch(E){a.sendError(E.message||"unknown")}if(G!=null&&G.length>0){r(B,C);m(B,G,D);B.at=c;B.d="Conv"}};var p=function(A,H,I){var G="link",B={},K={},F,C,J,E;try{B=l.actions[G].propertyMap}catch(D){a.sendError(D.message||"unknown")}if(I.bestWinObj!=null&&I.bestWinObj.document!=null){K=I.bestWinObj.document;F=K.URL;E=F.indexOf("?");if(E>-1){E=E+1;F=F.substring(E);C=q(F,"&","=");if(C!=null&&typeof C.dmtry!==b){J=C.dmtry;r(B,A);m(B,J,I);B.at=e;B.d="ClickLink"}}}};var r=function(A,B){A.jsv=B.ver||"na";A.rand=d(999999);A.sid=a.session;A.csync=(typeof A.csync!==b)?A.csync:1};var m=function(B,D,H){var C="na",G=l.config.TRANSLATE,A,J,E=y(D),H=H||v(),I=H.bestWinObj.document;for(J in E){if(E.hasOwnProperty(J)){A=J;if(typeof G[J]!==b){A=G[J]}B[A]=E[J]}}if(H.isTop===false){B["if"]=1;B.pg=I.referrer||C;B.chl=C}else{B.pg=I.URL||C;B.chl=I.referrer||C}if(E!=null&&typeof E.chl!==b&&E.chl.length>0){try{B.chl=decodeURIComponent(E.chl);B.chl_pass=1}catch(F){B.chl_pass=2}}};var y=function(A){if(A!=null&&typeof A==="string"){return q(A,";",":",true)}};var f=function(B,G,F,H){var C="",A,I,D,E=l.actions[F];A=t(B,G);I=z(B,E);D=k(B,E,H);if(A!=null&&I!=null&&D!=null&&A.length>0&&I.length>0&&D.length>0){C=A+I+D}return C};var t=function(B,C){var A=C.protocol||"http";A+="://";if(B.host!=null){A+=B.host+"/"}return A};var z=function(C,B){var F,E,D="",G=[],A=C.PATHORDER;for(F in A){if(A.hasOwnProperty(F)){E=A[F];G.push(B.propertyMap[E]||0)}}D+="redir/"+G.join("/")+"/1.ver";return D};var k=function(B,I,N){var N=(N===false)?false:true,E="",H=I.qsPropertyKeys,L=I.propertyMap,K=null,A,D,G=[],F=[],J=[],C=/^cus\./i;for(D=0;D<H.length;D++){K=H[D];A=L[K];if(A!=null&&typeof A!="function"){A=i(A);G.push(K+"="+A)}}if(N){for(K in L){if(L.hasOwnProperty(K)&&typeof L[K]!=="function"){if(!x(H,K)&&!x(l.config.PATHORDER,K)){F.push(K)}}}if(F.length>0){for(D=0;D<F.length;D++){K=F[D];A=L[K];if(K.search(C)>-1){G.push(K+"="+A)}else{J.push(K+"="+A)}}if(J.length>0){G.push("cus="+i(J.join(";")))}}}var M=B.SEND_ONCE;for(D=0;D<M.length;D++){if(typeof L[M[D]]!==b){delete L[M[D]]}}if(G.length>0){E+="?"+G.join("&")}return E};var i=function(B){if(B!=null&&typeof B!="function"){try{B=encodeURIComponent(B)}catch(A){B=escape(B)}}return B};var x=function(A,C){for(var B=0;B<A.length;B++){if(A[B]==C){return true}}return false};var q=function(C,B,J,E){if(C==null||C.length<1){return null}E=(E)?E:false;var K={},A=[],F=C.split(B),H,D,I,G;for(H=0;H<F.length;H++){D=F[H].indexOf(J);if(D>=0){I=F[H].substring(0,D);G=F[H].substring(D+1);K[I]=G}else{A.push(F[H]);F.splice(H,1);H--}}if(E){if(A.length>0){K.unk=A.join(";")}}return K};var n=function(){var A;if(l.config==null){throw new Error("invalid config")}l.scriptProps=o(l.config);w(l.config,l.scriptProps);if(l.isMaster===true){A=f(l.config,l.scriptProps,"link");a.sendRequest(A)}A=f(l.config,l.scriptProps,"refer");a.sendRequest(A)};a.directory.push(l);n()}catch(s){var j=s.message||"Unknown Channel Instance Error";if(typeof l.sendError!==b){l.sendError(j)}else{DMTRY.CHANNEL.sendError(j)}}})(a.directory.length)})()}catch(channelError){try{var msg=channelError.message||"Unknown Channel Error";DMTRY.CHANNEL.sendError(msg)}catch(lastEffortError){}};