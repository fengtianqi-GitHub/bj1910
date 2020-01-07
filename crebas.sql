/*==============================================================*/
/* DBMS name:      MySQL 5.0                                    */
/* Created on:     2020/1/7 16:25:00                            */
/*==============================================================*/


drop table if exists forum;

drop table if exists user;

/*==============================================================*/
/* Table: forum                                                 */
/*==============================================================*/
create table forum
(
   tid                  bigint not null,
   uid                  bigint,
   title                varchar(200),
   content              varchar(10000),
   create_date          datetime,
   primary key (tid)
);

/*==============================================================*/
/* Table: user                                                  */
/*==============================================================*/
create table user
(
   uid                  bigint not null,
   username             varchar(50) not null,
   password             char(128),
   primary key (uid)
);

alter table forum add constraint FK_Relationship_1 foreign key (uid)
      references user (uid) on delete restrict on update restrict;

