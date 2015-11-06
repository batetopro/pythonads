var ADS = ADS || {};
ADS.processing = false;
ADS.errors = 0;

ADS.set_preview = function(url, callback){
    console.log(url);

    var iframe = $('<iframe>');
    iframe.attr('width', '100%');
    iframe.attr('height', '600');
    iframe.attr('src', '/preview/' + url);

    if(callback){
        iframe.load(function(){
            callback();
        });
    }

    $('#ad-preview').html(iframe);

};


ADS.init = function(){
    ADS.ads = ADS.ads.split(',');

    var ad_list = $('#ad-list');
    ADS.ads.forEach(function(url){
        var cont = $("<li></li>");
        cont.text(url);
        cont.addClass("list-group-item");
        cont.on('click', function(){
            if(ADS.processing){return;}
            ADS.set_preview(url);
        });
        ad_list.append(cont);
    });

    $('#btn-process').on('click', function(){
        ADS.process();
    });
};

ADS.process = function(){
    if(ADS.ads.length == 0){return;}
    ADS.processing = true;
    $('#btn-process').hide();
    ADS.check(0);
}

ADS.check=function(idx){
    if(idx >= ADS.ads.length){
        if(ADS.errors){
            $('#btn-ok').addClass('btn-danger');
            $('#btn-ok').on('click', function(){
                alert('There are errors and queue can not be processed.');
            });
        }else{
            $('#btn-ok').addClass('btn-success');
            $('#btn-ok').on('click', function(){
                alert('Queue processed.');
            });
        }
        $('#btn-ok').show();
        ADS.processing = false;
        return;
    }

    var url = ADS.ads[idx];
    ADS.set_preview(url, function(){
        var ctr = 0;
        var interval = setInterval(function(){
            if(ctr == 0){
                $('#ad-list li').eq(idx).addClass('active');
            }else{
                $('#ad-list li').eq(idx).removeClass('active');
            }
            ctr = (ctr + 1) % 2;
        }, 250);

        $.get( '/check/'+url, function(resp){
            clearInterval(interval);
            if(resp == 'ok'){
                $('#ad-list li').eq(idx).addClass('list-group-item-success');
            }else{
                $('#ad-list li').eq(idx).addClass('list-group-item-danger');
                ADS.errors ++;
            }
            ADS.check(idx + 1);
        });
    });
}