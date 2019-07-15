FROM joyzoursky/python-chromedriver:3.6-xvfb

    USER root

    ENV SELENIUM_VERSION 3.6.0
    ENV PTEST_VERSION 1.9.5
    ENV VIOLENT_WEBDRIVER_VERSION 1.0.27
    ENV WORKING_DIR /test

    COPY uitest.py /test/
    RUN pip install --upgrade pip \
        && pip install selenium==${SELENIUM_VERSION} \
        && pip install ptest==${PTEST_VERSION}\
        && pip install violent-webdriver==${VIOLENT_WEBDRIVER_VERSION}

    ENTRYPOINT cd ${WORKING_DIR}; \
               xvfb-run --server-args="-screen 0 1024x768x24" ptest3 -t uitest