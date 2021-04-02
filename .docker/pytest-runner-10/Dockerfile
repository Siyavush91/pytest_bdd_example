FROM debian:buster

ENV DEBIAN_FRONTEND noninteractive
ENV DEBCONF_NONINTERACTIVE_SEEN true

# Set timezone
RUN echo "Europe/Moscow" > /etc/timezone && \
    dpkg-reconfigure --frontend noninteractive tzdata

# Create a default user
RUN groupadd --system automation && \
    useradd --system --create-home --gid automation --groups audio,video automation && \
    mkdir --parents /home/automation/reports && \
    chown --recursive automation:automation /home/automation


# Update the repositories
# Install dependencies
# Install utilities
# Install XVFB and TinyWM
# Install fonts
# Install Python
RUN apt-get -yqq update && \
    apt-get -yqq install gnupg2 \
    curl unzip \
    xvfb tinywm \
    fonts-ipafont-gothic xfonts-100dpi xfonts-75dpi xfonts-scalable xfonts-cyrillic \
    python python3-venv python3-pytest python3-tk python3-dev python3-selenium python3-wheel \
    gnupg-agent \
    software-properties-common \
    ffmpeg \
    default-jre && \
    rm -rf /var/lib/apt/lists/*

# Install Supervisor
RUN curl -sS -o - https://bootstrap.pypa.io/ez_setup.py | python && \
    easy_install -q supervisor

# Install Chrome WebDriver
RUN CHROMEDRIVER_VERSION=`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE` && \
    mkdir -p /opt/chromedriver-$CHROMEDRIVER_VERSION && \
    curl -sS -o /tmp/chromedriver_linux64.zip http://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip && \
    unzip -qq /tmp/chromedriver_linux64.zip -d /opt/chromedriver-$CHROMEDRIVER_VERSION && \
    rm /tmp/chromedriver_linux64.zip && \
    chmod +x /opt/chromedriver-$CHROMEDRIVER_VERSION/chromedriver && \
    ln -fs /opt/chromedriver-$CHROMEDRIVER_VERSION/chromedriver /usr/local/bin/chromedriver

# Install Google Chrome
RUN curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list && \
    apt-get -yqq update && \
    apt-get -yqq install google-chrome-stable && \
    rm -rf /var/lib/apt/lists/*

# Install Allure
#RUN add-apt-repository ppa:qameta/allure
#RUN apt-get -yqq install allure
#RUN curl -sS -o /tmp/allure-core.zip https://github.com/allure-framework/allure-core/releases/latest && \
#    unzip -qq /tmp/allure-core.zip -d /opt/allure
RUN curl -o /tmp/allure-commandline-2.13.6.tgz -Ls https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.13.6/allure-commandline-2.13.6.tgz && \ 
    tar -zxvf /tmp/allure-commandline-2.13.6.tgz -C /opt/ && ln -s /opt/allure-commandline-2.13.6/bin/allure /usr/bin/allure

RUN mkdir /opt/selenium
RUN curl -o /opt/selenium/selenium-server-standalone-3.141.59.jar -Ls https://selenium-release.storage.googleapis.com/3.141/selenium-server-standalone-3.141.59.jar

ENV PATH="$PATH:/opt/allure-2.13.6/bin"
RUN allure --version

# Configure Supervisor
ADD ./etc/supervisord.conf /etc/
ADD ./etc/supervisor /etc/supervisor

# Default configuration
ENV DISPLAY :20.0
ENV SCREEN_GEOMETRY "1440x900x24"
ENV CHROMEDRIVER_PORT 4444
ENV CHROMEDRIVER_WHITELISTED_IPS "127.0.0.1"
ENV CHROMEDRIVER_URL_BASE ''
ENV CHROMEDRIVER_EXTRA_ARGS ''

EXPOSE 4444

VOLUME [ "/var/log/supervisor" ]

CMD ["/usr/local/bin/supervisord", "-c", "/etc/supervisord.conf"]
