    function set_redis(key, value) {
        console.log("test")
        $.ajax({
            type: "POST",
            url: "/redis/set/" + key,
            data: JSON.stringify({ value: value }),
            dataType: "json",
            contentType: "json",
            success: function(data)
            {
                (data.GET);
            }
        });
    }

     function get_redis(key) {
        $.ajax({
            type: "GET",
            url: "redis/get/" + key,
            data: "format=json",
            dataType: "text",
            success: function(data)
            {
                $("#result").text(data.GET);
            }
        });
       }

      function split_string(string) {
            var string = str.split(" ",2);
            return string;
        };
