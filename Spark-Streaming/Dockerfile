# �⺻ �̹��� ����
# spark-3.3.1-bin-hadoop3/
# spark 3.3.1, scala 2.12 
FROM jupyter/all-spark-notebook:spark-3.3.1

# root ����ڷ� ��ȯ
USER root

# jovyan �׷� ���� �� �ش� �׷쿡 jovyan ����� �߰�
RUN groupadd jovyan && usermod -a -G jovyan jovyan 

# jovyan�� sudo ����ڷ� ����� �⺻ ��й�ȣ ����
# sudo ���� �ο�
# ��й�ȣ ����
ENV GRANT_SUDO=yes
RUN echo "jovyan ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers 
RUN echo "jovyan:jovyan" | chpasswd 

# ��Ű�� ������Ʈ �� �ʿ��� ��Ű�� ��ġ
RUN apt-get update -y && \
    apt-get install -y wget && \
    apt-get install -y default-jdk && \
    apt-get install netcat -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*


# Scala 2.12.14 �� sbt ��ġ
RUN wget https://downloads.lightbend.com/scala/2.12.14/scala-2.12.14.deb && \
    dpkg -i scala-2.12.14.deb && \
    apt-get update && \
    apt-get install -y scala && \
    wget https://github.com/sbt/sbt/releases/download/v1.5.5/sbt-1.5.5.tgz && \
    tar xzvf sbt-1.5.5.tgz && \
    mv sbt /usr/local && \
    echo "export PATH=/usr/local/sbt/bin:$PATH" >> /etc/bash.bashrc

# JDBC ��ġ
RUN cd /usr/local/spark-3.3.1-bin-hadoop3/jars && \
    if [ ! -f postgresql-42.6.0.jar ]; then \
        if ! wget -P /usr/local/spark-3.3.1-bin-hadoop3/jars https://jdbc.postgresql.org/download/postgresql-42.6.0.jar; then \
         echo "Failed to download PostgreSQL JDBC driver"; \
        fi \
    else \
        echo "PostgreSQL JDBC driver already exists"; \
    fi

# python ��Ű�� ��ġ
RUN pip install --no-cache-dir spylon-kernel py4j==0.10.9.5 && \
    python -m spylon_kernel install

# jars ���丮�� �������� jovyan���� ����
RUN chown -R jovyan:jovyan /usr/local/spark-3.3.1-bin-hadoop3/jars

# Python ��Ű�� ��ġ�� ���� jovyan���� �ٽ� ��ȯ
USER jovyan

# Jupyter Lab Ȱ��ȭ
ENV JUPYTER_ENABLE_LAB=yes

# ��Ʈ ����
EXPOSE 8888 4040 9999

# �۾� ���丮 ����
WORKDIR /home/jovyan

# ���� ����
VOLUME /home/jovyan

# Jupyter notebook ����
CMD ["start-notebook.sh"]