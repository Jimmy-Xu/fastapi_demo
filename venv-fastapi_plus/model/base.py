from sqlalchemy import Column, String, TIMESTAMP, text, DECIMAL, Date
from sqlalchemy.dialects.sqlite import DECIMAL, INTEGER, TEXT, SMALLINT
from sqlalchemy.ext.declarative import declarative_base

DeclarativeBase = declarative_base()


class Base(DeclarativeBase):
    """
    基础Model模型对象
    """
    __abstract__ = True

    id = Column(DECIMAL(20), primary_key=True, comment='序号')
    parent_id = Column(DECIMAL(20), nullable=False, server_default=text("0"), comment='父序号')
    type = Column(INTEGER, nullable=False, server_default=text("0"), comment='类型')
    sort = Column(INTEGER, nullable=False, server_default=text("0"), comment='排序')
    status = Column(SMALLINT, nullable=False, server_default=text("0"), comment='状态')
    is_deleted = Column(SMALLINT, nullable=False, server_default=text("0"), comment='软删')
    created_by = Column(DECIMAL(20), nullable=False, server_default=text("0"), comment='创建人')
    created_time = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"), comment='创建时间')
    updated_by = Column(DECIMAL(20), nullable=False, server_default=text("0"), comment='更新人')
    updated_time = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"), comment='更新时间')
    code = Column(String(255), nullable=False, server_default=text("''"), comment='编码')
    name = Column(String(255), nullable=False, server_default=text("''"), comment='名称')
    label = Column(String(255), nullable=False, server_default=text("''"), comment='标签')
    logo = Column(String(255), nullable=False, server_default=text("''"), comment='图标')
    url = Column(String(255), nullable=False, server_default=text("''"), comment='URL')
    info = Column(String(1000), nullable=False, server_default=text("''"), comment='内容')
    remark = Column(String(1000), nullable=False, server_default=text("''"), comment='备注')
    search = Column(TEXT, comment='搜索')
