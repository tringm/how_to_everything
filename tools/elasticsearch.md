## Elasticsearch guide

### Set up
1. Sources:
    * [Debian](https://www.elastic.co/guide/en/elasticsearch/reference/current/deb.html)
        * Download
        * ```sudo dpkg -i elasticsearch-6.6.1.deb```
        * Check if system uses SysV ```init``` or ```systemd``` with ```ps -p 1```
        * With:
            * ***init***:
                * Use the update-rc.d command to configure Elasticsearch to start automatically when the system boots up:
                ```
                sudo update-rc.d elasticsearch defaults 95 10
                ```
                * Elasticsearch can be started and stopped using the service command:
                ```
                sudo -i service elasticsearch start
                sudo -i service elasticsearch stop
                ```
                * If Elasticsearch fails to start for any reason, it will print the reason for failure to STDOUT. Log files can be found in /var/log/elasticsearch/.
            * ***systemd***:
                *  To configure Elasticsearch to start automatically when the system boots up, run the following commands:
                ```
                sudo /bin/systemctl daemon-reload
                sudo /bin/systemctl enable elasticsearch.service
                ```
                * Elasticsearch can be started and stopped as follows:
                ```
                sudo systemctl start elasticsearch.service
                sudo systemctl stop elasticsearch.service
                ```
                * These commands provide no feedback as to whether Elasticsearch was started successfully or not. Instead, this information will be written in the log files located in /var/log/elasticsearch/.

                * By default the Elasticsearch service doesn’t log information in the systemd journal. To enable journalctl logging, the --quiet option must be removed from the ExecStart command line in the elasticsearch.service file.

                * When systemd logging is enabled, the logging information are available using the journalctl commands:
                    * To tail the journal:
                    ```
                    sudo journalctl -f
                    ```
                    * To list journal entries for the elasticsearch service:
                    ```
                    sudo journalctl --unit elasticsearch
                    ```
                    * To list journal entries for the elasticsearch service starting from a given time:
                    ```
                    sudo journalctl --unit elasticsearch --since  "2016-10-30 18:17:16"
                    ````
                    Check man journalctl or https://www.freedesktop.org/software/systemd/man/journalctl.html for more command line options.
        * Check that elasticsearch is running:
        ```
        curl GET localhost:9200
        ```
