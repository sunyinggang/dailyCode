package com.syg.yiqing.entity;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import javax.persistence.*;
import java.awt.*;
import java.sql.Date;

@Data
@NoArgsConstructor
@AllArgsConstructor
@Entity
@Table(name = "bidding_ggzy")
public class BiddingGgzy {
    @Id // 该字段对应数据库中的列为主键
    @GeneratedValue(strategy = GenerationType.IDENTITY) // 主键自增长
    @Column(name = "id") // 对应tradition_office表中的id列
    private Integer id;

    @Column(name = "bidding_people")
    private String bidding_people;

    @Column(name = "name")
    private String name;

    @Column(name = "field")
    private String field;

    @Column(name = "begin_date")
    private Date begin_date;

    @Column(name = "money")
    private Float money;

    @Column(name = "company")
    private String company;

}
